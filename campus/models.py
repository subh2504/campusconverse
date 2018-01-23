from django.db import models

# Create your models here.

class CampusDetail(models.Model):
    campus_id = models.IntegerField(primary_key=True)
    campus_owner = models.For
    campus_name = models.CharField(max_length=100)
    campus_address = models.CharField(max_length=100,blank=True,null=True)
    campus_locality = models.CharField(max_length=100,blank=True,null=True)
    campus_city = models.CharField(max_length=20,blank=True,null=True)
    campus_country = models.CharField(max_length=20,blank=True,null=True)
    campus_pincode = models.CharField(max_length=6,blank=True,null=True)
    campus_logo = models.CharField(max_length=15)

    def __str__(self):
        return self.campus_name
        
        
class MasterDepart(models.Model):
    depart_id = models.IntegerField(primary_key=True)
    depart_name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.depart_name


class MasterCourse(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.course_name

class Desination(models.Model):
    designation_id = models.IntegerField(primary_key=True)
    designation_name = models.CharField(unique=True, max_length=50)
    type = models.IntegerField()

    def __str__(self):
        return self.designation_name
        
        
class CampusCourseDepart(models.Model):
    ccd_id= models.IntegerField(primary_key=True)
    campus = models.ForeignKey('CollegeDetail')
    course = models.ForeignKey('MasterCourse')
    department = models.ForeignKey('MasterDepart')

    def __str__(self):
        return self.college.college_name + " " + self.course.course_name + " " + self.depart.depart_name