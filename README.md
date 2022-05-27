# Carnot

<!-- python manage.py migrate --run-syncdb -->

### Below postgress command updates the sequence of table student
```SELECT setval('library_student_id_seq', (SELECT MAX(id) from "library_student"));```