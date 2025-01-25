from django.db import models

# Create your models here.


class Userdata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self): 
        return self.email 
class Studentinfo(models.Model):
    student_name=models.CharField(max_length=100)
    student_image=models.ImageField(upload_to='doctors/')
    specialization=models.CharField(max_length=100)


    def __str__(self):
        return self.student_name_name    
