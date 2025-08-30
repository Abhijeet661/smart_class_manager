from django.http import JsonResponse, HttpResponse
from .models import Classroom, Student
from django.views.decorators.csrf import csrf_exempt
import json

# GET list of classrooms
def classroom_list(request):
    if request.method == "GET":
        classrooms = list(Classroom.objects.values('id', 'name', 'teacher_name'))
        return JsonResponse(classrooms, safe=False)
    return HttpResponse(status=405)

# GET list of students or CREATE new student
@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = list(Student.objects.values('id', 'name', 'age', 'classroom_id'))
        return JsonResponse(students, safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            classroom = Classroom.objects.get(id=data["classroom_id"])
            student = Student.objects.create(
                name=data["name"],
                age=data["age"],
                classroom=classroom
            )
            return JsonResponse({"id": student.id, "name": student.name, "age": student.age, "classroom_id": classroom.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return HttpResponse(status=405)

# GET, UPDATE, DELETE a single student
@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)

    if request.method == 'GET':
        return JsonResponse({"id": student.id, "name": student.name, "age": student.age, "classroom_id": student.classroom.id})

    elif request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            student.name = data.get("name", student.name)
            student.age = data.get("age", student.age)
            classroom_id = data.get("classroom_id", student.classroom.id)
            if classroom_id != student.classroom.id:
                student.classroom = Classroom.objects.get(id=classroom_id)
            student.save()
            return JsonResponse({"id": student.id, "name": student.name, "age": student.age, "classroom_id": student.classroom.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)

    return HttpResponse(status=405)