# Student-Enrollment
student enrolment but without page refresh using AJAX in a django app. In the same app performs CSV and PDF generation for any models created in the student enrollment activity
#steps

Create a new Django project and app:
bash
Copy code
django-admin startproject student_enrollment
cd student_enrollment
python manage.py startapp enrollment

Install required packages:
bash
pip install reportlab

Run migrations:
bash
python manage.py makemigrations
python manage.py migrate

Create a superuser to access the Django admin:
bash
python manage.py createsuperuser

Start the development server:
bash
python manage.py runserver
