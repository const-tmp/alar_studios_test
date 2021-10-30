# alar_studios_test
Тестовое задание для Alar Studios

## Установка
```
git clone https://github.com/h1ght1me/alar_studios_test.git
cd alar_studios_test
docker-compose up
```

## Описание
```
git clone https://github.com/h1ght1me/alar_studios_test.git
cd alar_studios_test
```
потом
```
docker-compose up
```
или
```
pip install .
export FLASK_APP=alar_studios_test.app
flask run
```
или
```
pip install .
pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:5000 'alar_studios_test.app:create_app()' --preload
```

Мини приложение для просмотра и редактирования списка пользователей. Реализовано на Flask.

Начальный пользователь в базе username: root password: toor

У каждого пользователя есть права чтения/создания/редактирования/удаления. Право на чтение есть у всех.

Пользователь не может создать/изменить пользоователя с большими правами, чем он имеет. Пользователь не может
редактировать свои права.

Логин, создание и удаление пользователей как через форму так и через REST API. Редактирование прав через AJAX и REST
API.

Аутентификация как по Cookie так и по токену (упрощенная, чтобы не использовать сторонние библиотеки).

### Конечные точки

#### Логин

/auth/login

#### Страница пользователей

/users

#### Задание №2

/json

## Возможные улучшения

- Полноценная аутентификация по JWT
- Валидация данных в формах и API
- Пагинация
- .env не должен быть в контроле версий, но это тестовое задание
