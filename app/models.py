from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    college = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):

    SECTION_CHOICES = (
        ('Aptitude', 'Aptitude'),
        ('Technical', 'Technical'),
        ('Grammar', 'Grammar'),
    )

    section = models.CharField(max_length=20, choices=SECTION_CHOICES)

    question = models.TextField()

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Result(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    section = models.CharField(max_length=20)

    score = models.IntegerField()

    status = models.CharField(max_length=20)

    def __str__(self):
        return self.student.name