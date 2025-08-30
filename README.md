Smart Class Manager

A full-stack project with Django (Backend) and React (Frontend)


🔹 Project Overview

Smart Class Manager is a web application to manage students, teachers, and batches for an educational institute.

Features include:
	•	Add Students (Name, Age, Batch)
	•	Add Teachers
	•	View all added Students and Teachers
	•	Batch management for easy grouping
	•	Clean professional interface


🔹 Tech Stack
•	Backend: Django, Django REST Framework
•	Frontend: React.js, HTML, CSS
•	Database: SQLite
•	Other Tools: Git, npm, virtualenv

🔹 How to Run Locally

1️⃣ Clone Repository

git clone https://github.com/Abhijeet661/smart_class_manager.git
cd smart_class_manager

2️⃣ Setup Backend (Django)

cd backend
python3 -m venv venv       # Create virtual environment if not already
source venv/bin/activate
pip install -r requirements.txt  # Install dependencies
python3 manage.py migrate
python3 manage.py runserver

Open: http://127.0.0.1:8000


3️⃣ Setup Frontend (React)

cd ../frontend
npm install
npm start

Open: http://localhost:3000


🔹 Project Structure

smart_class_manager/
├── backend/           # Django backend
│   ├── backend/       # Django project files
│   └── classroom_app/ # App for student, teacher, batch
├── frontend/          # React frontend
├── venv/              # Python virtual environment
├── db.sqlite3         # SQLite database
└── package-lock.json  # npm dependencies


🔹 Features Implemented
	•	Add Students (Name, Age, Batch)
	•	Add Teachers
	•	Display all Students and Teachers
	•	Batch selection while adding students
	•	Professional UI design with CSS

⸻

🔹 Future Implementation Ideas
	•	Login system for teachers/admin
	•	Attendance tracking
	•	Batch-wise report generation
	•	Notification system for students/teachers
	•	Full responsive design


