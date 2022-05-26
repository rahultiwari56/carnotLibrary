from django.db import models


class Student(models.Model):

    gender_choice = [
        ('Male','Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=25, choices=gender_choice, default='Prefer not to say')
    school = models.ForeignKey(
        'School', to_field='school_id', null=True, blank=True, on_delete=models.SET_NULL, default=None)
    book = models.ForeignKey(
        'Book', to_field='book_id', null=True, blank=True, on_delete=models.SET_NULL, default=None)

    def __str__(self):
        return f'({self.id}) {self.first_name}'


class School(models.Model):

    school_id = models.AutoField(primary_key=True)
    region_id = models.IntegerField()
    school = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.TextField(max_length=80)

    def __str__(self):
        return f'({self.school_id}) {self.school}'


class Book(models.Model):

    book_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Author_Name = models.CharField(max_length=50, blank=True, null=True)
    Date_Of_Publication = models.DateField(blank=True, null=True)
    Number_Of_Pages = models.IntegerField()

    def __str__(self):
        return f'({self.book_id}) {self.Title}'