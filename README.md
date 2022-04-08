# WhatToDo_API
API for my future ToDo web abb created with Django Rest Framework

## Planned feautures status (can be changed in future):
- [ ] User authentication and authorization
- [ ] CRUD operations with tasks
- [ ] Notifications using telegram-bot

## Environment configuration:
- `git clone <repo>`
- `cd WhatToDo_API`
- `pip install virtualenv`
- `virtualenv <virtual environment name>` 
- `source <virtual environment name>/bin/activate`
- `pip install -r requirements.txt`
- `cd whattodo_api/whattodo_api`
- Create file called .env with following content:
  ```
  DATABASE_NAME=<NAME_OF_PREVIOUSLY_CREATED_DB>
  DATABASE_USER=<NAME_OF_DB_USER>
  DATABASE_PASSWORD=<PASSWORD_FOR_DB_USER>
  DATABASE_HOST=<HOST_OF_YOUR_DATABASE>
  DATABASE_PORT=<PORT_OF_YOUR_HOST>
  ```
- Now, you are ready to GO! You can run server with `python manage.py runserver`.
