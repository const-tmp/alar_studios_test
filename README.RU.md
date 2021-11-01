# alar_studios_test

Тестовое задание для Alar Studios

## Установка

```
git clone https://github.com/h1ght1me/alar_studios_test.git
cd alar_studios_test
```

Далее создайте файл .env и заполните **необходимые** данные:

```
echo 'POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=alar

SESSION_DURATION=1800
  
APP_PORT=5000' > .env

```

потом

```
docker-compose up
```

или

```
virtualenv venv
source venv/bin/activate
pip install .
export FLASK_APP=alar_studios_test.app
flask run
```

или

```
virtualenv venv
source venv/bin/activate
pip install .
pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:5000 'alar_studios_test.app:create_app()' --preload
```

### Запуск без Docker

Для запуска не в докере вам нужна работающая база Postgres. Перед запуском нужно
запустить [команды](src/alar_studios_test/sql/init.sql)

## Описание

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
- Nginx
