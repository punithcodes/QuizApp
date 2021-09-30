from django.db import models

CATEGORY_CHOICES = (
    ('Maths', 'Maths'),
    ('Science', 'Science'),
    ('English', 'English'),
)

# Here I have created class Quiz model which is responsible to store questions, options and answer in the database.
class Quiz(models.Model):
    subject = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    question = models.CharField(max_length=200)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    answer = models.CharField(max_length=1)


# This class is responsible to store the related information of the completed quiz in the database.
class Result(models.Model):
    student = models.CharField(max_length=100)
    subject = models.CharField(max_length=20)
    marks = models.IntegerField()
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=50)
