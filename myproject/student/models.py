from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(5, message="Age must be at least 5"), MaxValueValidator(30, message="Age must be at most 30")])
    email = models.EmailField(unique=True)
    image = models.ImageField(null=True, upload_to='student_image')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
