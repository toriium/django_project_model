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


# Other 
RUN python manage.py collectstatic --noinput

# Run server
python manage.py runserver


# To existing DB
- Add DB connections values
- run `python manage.py migrate` to generate django tables
- Inspect the DB and add tables to models with `managed = False` 
- Add the tables to admin
- Run python manage.py runserver

## Check
`managed = False` in the tables

- run `python manage.py makemigrations`
- check the migration generated

## Check the operations that will be execute
python manage.py sqlmigrate <app> 0001
You need to see something like this
```
BEGIN;
--
-- Create model TblProduct
--
-- (no-op)
COMMIT;
```
with "(no-op)", this means will not execute any command in the DB


run `python manage.py migrate`