from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	Name = models.CharField(max_length = 100)
	DOB=models.DateField()
	Institution = models.CharField(max_length = 100)
	Qualification=models.CharField(max_length=100)
	YearOfPassing = models.IntegerField()
	
	def __str__(self):
		return self.user.username

class Experience(models.Model):
	exp_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	company = models.CharField(max_length=100, default="")
	job_profile = models.CharField(max_length=50)
	work_experience = models.CharField(max_length=50)
	isApproved = models.BooleanField(default= False)
	
	def __str__(self):
		return self.user.username

class RoundDetails(models.Model):
	r_id = models.AutoField(primary_key=True)
	exp_id = models.ForeignKey(Experience,on_delete=models.CASCADE)
	duration = models.PositiveIntegerField()
	about = models.TextField(max_length=500)



    