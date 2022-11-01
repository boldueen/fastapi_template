FROM python:3.10


WORKDIR /code/

COPY . /code/

COPY requirements.txt /code/
RUN pip install -r requirements.txt

EXPOSE 1488


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1488", "&&", "alembic", "upgrade", "head"]
