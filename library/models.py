from django.db import models


class Student(models.Model):

    gender_choice = [
        ('Male','Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    ]

    # student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(
        max_length=25, choices=gender_choice, default='Prefer not to say')
    school = models.ForeignKey(
        'School', to_field='id', null=True, blank=True, on_delete=models.SET_NULL, default=None)
    book = models.ForeignKey(
        'Book', to_field='id', null=True, blank=True, on_delete=models.SET_NULL, default=None)

    def __str__(self):
        return f'({self.id}) {self.first_name}'


class School(models.Model):

    # school_id = models.AutoField(primary_key=True)
    region_id = models.IntegerField(blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    principal = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(max_length=80, blank=True, null=True)

    def __str__(self):
        return f'({self.id}) {self.school}'


class Book(models.Model):

    # book_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Author_Name = models.CharField(max_length=50, blank=True, null=True)
    Date_Of_Publication = models.DateField(blank=True, null=True)
    Number_Of_Pages = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'({self.id}) {self.Title}'