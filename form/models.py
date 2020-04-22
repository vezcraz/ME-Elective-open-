from django.db import models

class stuCourseData(models.Model):
	CampusID  = models.CharField(max_length=100)
	Name= models.CharField(max_length=100)
	CourseCode = models.CharField(max_length=15)

	def __str__(self):
		return self.CampusID



class courseOffered(models.Model):
	CourseCode = models.CharField(max_length=15)
	Tag  = models.CharField(max_length=100)
	CourseName= models.CharField(max_length=100)

	def __str__(self):
		return self.CourseCode


class cdc(models.Model):
	CourseCode= models.CharField(max_length=100)
	CourseName=models.CharField(max_length=150)
	Year= models.CharField(max_length=10)
	Sem=models.CharField(max_length=5)
	def __str__(self):
		return self.CourseName

class courseList(models.Model):
	BranchCode= models.CharField(max_length=100)
	CourseCode= models.CharField(max_length=10)
	CourseName=models.CharField(max_length=150)
	Type=models.CharField(max_length=10)
	def __str__(self):
		return self.CourseName
class regSem(models.Model):
	Academic_year_start = models.CharField(max_length=4)
	Registration_for_sem = models.CharField(max_length=2)

# class StuData(models.Model):
# 	CampusID  = models.CharField(max_length=100)
# 	Name= models.CharField(max_length=100)
# 	Subject = models.CharField(max_length=15)

# 	def __str__(self):
# 		return self.CampusID

# class CourseOffered(models.Model):
# 	Subject= models.CharField(max_length=100)
# 	Code= models.CharField(max_length=10)
# 	CourseName=models.CharField(max_length=150)

# 	def __str__(self):
# 		return self.CourseName

# class CourseList(models.Model):
# 	Subject= models.CharField(max_length=100)
# 	Code= models.CharField(max_length=10)
# 	CourseName=models.CharField(max_length=150)
# 	Year=models.IntegerField()
# 	Sem=models.IntegerField()

# 	def __str__(self):
# 		return self.CourseName

