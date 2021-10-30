# alar_studios_test
Test task for Alar Studios

[Описание на русском](README.RU.md)
## Quickstart
```
git clone https://github.com/h1ght1me/alar_studios_test.git
cd alar_studios_test
```
then
```
docker-compose up
```
or
```
pip install .
export FLASK_APP=alar_studios_test.app
flask run
```
or
```
pip install .
pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:5000 'alar_studios_test.app:create_app()' --preload
```

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
- .env file shouldn't be in VC
