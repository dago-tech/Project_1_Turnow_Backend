# Turnow Project


<img src="https://www.thetestspecimen.com/img/django-initial/django-rest-logo-960w.jpg" alt="django rest framework" width="130" height="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain-wordmark.svg" alt="postgresql" width="65" height="65"/>

This is the backend section of Turnow Project. In docs folder you can find information about explanation, design and architecture.

This API will allow you to interact with a generic turn management system, a person (client) approaches a computer, enters his personal id and other data about his necessity, receives a turn number, then he should wait for his turn to be shown in the notification screen, after that he will be able to be served in one the service desks by a person called 'user'.

## Commands

- Create and build the virtual environment in bash console:

```sh
py -m venv venv
source venv/Scripts/activate
```

- Install dependencies:

```sh
pip install -r requirements.txt
```

- Try the Django local server:

```sh
py manage.py runserver
```


## API

__Permissions__:

1. To access to the endpoints, a superuser must be created

```sh
py manage.py createsuperuser
```

2. Create an admin user:
```json
POST - /api/user/create/

{
    "email": "",
    "user_name": "",
    "password": "",
    "last_login": null,
    "first_name": "",
    "last_name": "",
    "is_admin": true,
    "is_active": true,
    "is_staff": true
}
```

3. This admin user will be able to create another users taking into account that *"is_active" = true* means that user has an admin role and *"is_active" = false* means the user has and service desk role (see "02_Use cases" document).


__End-points__:

Let's present the endpoints used to interact to the system and see its functionalities:

1. First of all, admin should do the initial set up and establish users, categories, priorities and service desks:

- Create a __user__:

```json
POST - /api/user/create/
{   
    "email": "",
    "user_name": "",
    "password": "",
    "last_login": null,
    "first_name": "",
    "last_name": "",
    "is_admin": false,
    "is_active": true,
    "is_staff": true
}
```
- List  __users__:

```json
GET - /api/user/
```

- Update a __user__:

```json
PUT-PATCH - /api/user/update/id/
```

- Delete a __user__:

```json
DELETE - /api/user/delete/id/
```

- Create a __category__:

```json
POST - /api/category/create/
{   
    "name": "",
    "description": ""
}
```

- Create a __priority__, priority must be a number between 0 and 20(highest priority):

```json
POST - /api/priority/create/
{   
    "name": "",
    "description": "",
    "priority": ""
}
```

- Create a __service_desk__:

```json
POST - /api/desk/create/
{   
    "name": "",
    "user": "",
    "category": "",
    "state": "",
    "busy": "",
}
```

2. When a client arrives at the establishment, he will enter some data to the system and a client and a turn register will be created in the database. Turn will be created with field "state" equals to "pending":

- Create a __client__:

```json
POST - /api/client/create/
{   
    "id_type": "",
    "personal_id": ""    
}
```

- Create a __turn__:

```json
POST - /api/turn/create/
{   
    "personal_id": "",
    "category": "",
    "priority": "",  
}
```

- Retrieve a __turn__:

```json
GET - /api/turn/id/

response:
{
    "id": 7,
    "turn_number": "A004",
    "created": "2023-11-14T11:56:34.465636-05:00",
    "start_time": null,
    "end_time": null,
    "duration": null,
    "waiting_time": null,
    "state": "pending",
    "personal_id": 3,
    "category": 1,
    "priority": 1,
    "desk": null
}
```

- List of __turns__:

```json
GET - /api/turn/
```

3. After a waiting time, one or more service desk will request to serve a client, client's turn will be choose based on priority, category and turn creation time. Turn.state will be updated to "first to serve":
```json
PUT - api/turn/serve/<int:desk_id>/

Turn instance response:
{
    "id": 4,
    "turn_number": "A001",
    "created": "2023-11-13T22:28:04.648374-05:00",
    "start_time": null,
    "end_time": null,
    "duration": null,
    "waiting_time": null,
    "state": "first to serve",
    "personal_id": 1,
    "category": 1,
    "priority": 1,
    "desk": 1
}

```

4. Client will come to service desk, then user will check the turn number typing it into the system, if it is correct Turn instance will be updated and user will be able to serve the client. Turn.state will be updated to "serving":

```json
PUT - api/turn/serving/<int:desk_id>/
{   
    "turn_number": "A001",  
}
Turn instance response:
{
    "id": 4,
    "turn_number": "A001",
    "created": "2023-11-13T11:03:04.648374-05:00",
    "start_time": "11:13:14.345258",
    "end_time": null,
    "duration": null,
    "waiting_time": 10,
    "state": "serving",
    "personal_id": 1,
    "category": 1,
    "priority": 1,
    "desk": 1
}
```
- Also desk state is updated:
```json
PATCH - api/desk/update/<int:desk_id>/
{   
    "busy": true,  
}
Desk instance response:
{
    "id": 1,
    "name": "Modulo 1",
    "state": true,
    "busy": true,
    "user": 1,
    "category": [
        1,
        2
    ]
}
```

5. When user finishes to serve the client, turn and desk registers should be updated:

```json
PUT - api/turn/served/<int:desk_id>/

Turn instance response:
{
    "id": 4,
    "turn_number": "A001",
    "created": "2023-11-13T11:03:04.648374-05:00",
    "start_time": "11:13:14.345258",
    "end_time": "11:19:42.385570",
    "duration": 6,
    "waiting_time": 10,
    "state": "served",
    "personal_id": 1,
    "category": 1,
    "priority": 1,
    "desk": 1
}
```

```json
PATCH - api/desk/update/<int:desk_id>/
{   
    "busy": false,  
}
Desk instance response:
{
    "id": 1,
    "name": "Modulo 1",
    "state": true,
    "busy": false,
    "user": 1,
    "category": [
        1,
        2
    ]
}
```

__API Documentation__

You can access to API documentation based on Swagger and coreapi at the link:

```
/docs/
```