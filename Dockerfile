
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --deploy --system --ignore-pipfile

COPY . .

CMD ['uvicorn', 'app.main:app', '--reload', '--port', '8000']