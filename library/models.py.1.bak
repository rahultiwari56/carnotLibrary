from django.db import models


class Student(models.Model):

    gender_choice = [
        ('Male'),
        ('Female'),
        ('Prefer not to say'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=25, choices=gender_choice, default='Prefer not to say')
    school_id = models.ForeignKey(
        'School', to_field='id', null=True, on_delete=models.SET_NULL)
    book_id = models.ForeignKey(
        'Book', to_field='id', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' (' + str(self.id) + ')'


class School(models.Model):

    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=50)

    def __str__(self):
        return self.school_name + ' (' + str(self.id) + ')'


class Book(models.Model):

    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50)

    def __str__(self):
        return self.book_name + ' (' + str(self.id) + ')'