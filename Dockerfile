FROM python:3.9

WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONPATH=/code

COPY . /code/

RUN pip install gunicorn

RUN pip install .

ENTRYPOINT gunicorn -w 4 -b "0.0.0.0:${APP_PORT}" 'alar_studios_test.app:create_app()' --preload
