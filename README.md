# alar_studios_test
Test task for Alar Studios

## Quickstart
```
git clone https://github.com/h1ght1me/alar_studios_test.git
cd alar_studios_test
docker-compose up
```

## Description
Mini app for viewing and editing list of users. Implemented with Flask.

Iitial username: root password: toor

Every user has permissions for read/create/update/delete. Every user can read.

User can't create or set permissions that he hasn't. User can't edit his own permissions.

Login, creating and deleting users available with either wob form or RESP API. Editing permissions with AJAX and REST API.

Cookie and Token authentication. Token auth is dummy for using less imports.

## Improvements
- JWT Auth
- Validation
- Pagination
- .env file shouldn't be in VC
