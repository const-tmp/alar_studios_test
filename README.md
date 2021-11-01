# alar_studios_test

Test task for Alar Studios

[Описание на русском](README.RU.md)

## Quickstart

```
git clone https://github.com/h1ght1me/alar_studios_test.git
cd alar_studios_test
```

Then fill in .env file with **required** credentials

```
echo 'POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=alar

SESSION_DURATION=1800
  
APP_PORT=5000' > .env

```

then

```
docker-compose up
```

or

```
virtualenv venv
source venv/bin/activate
pip install .
export FLASK_APP=alar_studios_test.app
flask run
```

or

```
virtualenv venv
source venv/bin/activate
pip install .
pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:5000 'alar_studios_test.app:create_app()' --preload
```

### Non-docker run

For non-docker run you need running postgres instance and to initialize database,
executing [commands](src/alar_studios_test/sql/init.sql)

## Description

Mini app for viewing and editing list of users. Implemented with Flask.

Iitial username: root password: toor

Every user has permissions for read/create/update/delete. Every user can read.

User can't create or set permissions that he hasn't. User can't edit his own permissions.

Login, creating and deleting users available with either wob form or RESP API. Editing permissions with AJAX and REST
API.

Cookie and Token authentication. Token auth is dummy for using less imports.

### Endpoints

#### Login

/auth/login

#### Users

/users

#### Task №2

/json

## Improvements

- JWT Auth
- Validation
- Pagination
- Nginx
