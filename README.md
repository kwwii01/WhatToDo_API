# WhatToDo_API
API for my future ToDo web abb created with Django Rest Framework

## Planned feautures status (can be changed in future):
- [x] User authentication and authorization
- [x] CRUD operations with tasks
- [ ] Notifications using telegram-bot

## Environment configuration:
- Install virtualenv package `pip install virtualenv`
- Create new virtual environment in repository folder `virtualenv <virtual environment name>` 
- Activate newly created venv:
  - In Terminal: `source <virtual environment name>/bin/activate`
  - In PowerShell: `<virtual environment name>/Scripts/Activate.ps1`
  - In CMD: `<virtual environment name>/Scripts/activate.bat`
- Install all necessary python packages `pip install -r requirements.txt`
- Go to Django project folder `cd whattodo_api`
- Apply migrations to your database `python manage.py migrate` 
- Insert initial data to your database:
  - Insert priorities: `python manage.py loaddata priorities.json`
  - Insert statuses: `python manage.py loaddata statuses.json`
- Go to core app folder `cd whattodo_api/`
- Create file called .env with following content:
  ```
  DATABASE_NAME=<NAME_OF_PREVIOUSLY_CREATED_DB>
  DATABASE_USER=<NAME_OF_DB_USER>
  DATABASE_PASSWORD=<PASSWORD_FOR_DB_USER>
  DATABASE_HOST=<HOST_OF_YOUR_DATABASE>
  DATABASE_PORT=<PORT_OF_YOUR_HOST>
  ```
- Go back to your `manage.py` file `cd ..`
- Now, you are ready to GO! You can run server with `python manage.py runserver`.
