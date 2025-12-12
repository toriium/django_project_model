# django_project_model

# Commands
django-admin startproject core .
python manage.py startapp <app_name>

# Create Admin user
python manage.py createsuperuser

# ORM Migrations
python manage.py makemigrations
python manage.py migrate
python manage.py inspectdb > inspect_models.py


# Run server
python manage.py runserver


# To existing DB
- Add DB connections values
- run `python manage.py migrate` to generate django tables
- Inspect the DB and add tables to models with `managed = False` 
- Add the tables to admin
- Run python manage.py runserver


pkgs:
- django-jazzmin - Admin
- django-advanced-filters - Admin