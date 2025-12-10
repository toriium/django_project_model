# django_project_model

# Commands
django-admin startproject core .
cd core
python manage.py startapp <app_name>

# Create Admin user
python manage.py createsuperuser

# ORM Migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver