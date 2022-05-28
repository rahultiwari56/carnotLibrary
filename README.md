# Carnot

<!-- python manage.py migrate --run-syncdb -->

### Below postgress command updates the sequence of table student
```SELECT setval('library_student_id_seq', (SELECT MAX(id) from "library_student"));```

### Running project via Docker
- Make sure you have installed docker and docker compose
- Create db and update it to the env file

- Run below command

1.Build Image

```docker-compose build```

2.Run Docker image

```docker-compose up```

<br>

# Project setup on system
<br>
<strong>1. Install the libraries </strong>

- preferred installing libraries in a python environment : <a href="https://docs.python.org/3/library/venv.html">Follow Steps</a>

```pip install requirements.txt```

<br>

<strong>2. create database </strong>
- Create a database and update the credentials in next step

<br>

<strong>3. Update the env file </strong>

```
-> DBNAME
-> DBUSER
-> DBPASSWORD
-> DBHOST
-> DBPORT
```

<br>

<strong>3. db migrations </strong>

#### Run below 2 commands:
1. ```python manage.py makemigrations```


2. ```python manage.py migrate```

<br>

<strong>4. Create Super User </strong>

```python manage.py createsuperuser```

<br>

<strong>5. Run the ETL </strong>
- Here the raw data from file need to be pre-processed and transfer to the db
- Move to ```dbOps/``` and thanrun the below command
```pyhton xlstosql.py```

<br>

<strong>6. Run the Project </strong>
```python manage.py runserver```

<br>

Note: Please check the project ```settings.py``` make sure if evrything is updated.