from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=100)
    duration=models.CharField(max_length=50, default='3 months')
    about_course=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.title

GENDER_CHOICE = (
    ('M', 'male'),
    ('F', 'female')
)


class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.PositiveBigIntegerField()
    gender= models.CharField(max_length=2, choices=GENDER_CHOICE, default='M')
    email = models.EmailField(max_length=30)
    # phone = models.BigIntegerField()
    # address = models.TextField()
    # join_date = models.DateTimeField('Registration date')
    # end_date = models.DateTimeField('Graduation Date')
    # course=models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
class Admission(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    is_verified=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.firstname} {self.student.lastname} registered'
    
class Instructor(models.Model):
    name = models.CharField(max_length=40)
    email=models.EmailField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    gender= models.CharField(max_length=2, choices=GENDER_CHOICE, default='M')

    def __str__(self):
        return self.name
    
