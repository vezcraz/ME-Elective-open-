from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student_Info(models.Model):
	user= models.OneToOneField(User, on_delete = models.CASCADE)
	Identity= models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	# p1=models.CharField(max_length=100, null=True)
	# p2=models.CharField(max_length=100, null=True)
	# p3=models.CharField(max_length=100, null=True)
	# p4=models.CharField(max_length=100, null=True)
	p=models.CharField(max_length=1000)



	

