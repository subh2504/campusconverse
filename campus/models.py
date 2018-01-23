from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe

from campusconverse import settings


class CampusDetail(models.Model):
    campus_id = models.AutoField(primary_key=True)
    campus_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    campus_name = models.CharField(max_length=100)
    campus_address = models.CharField(max_length=100, blank=True, null=True)
    campus_locality = models.CharField(max_length=100, blank=True, null=True)
    campus_city = models.CharField(max_length=20, blank=True, null=True)
    campus_country = models.CharField(max_length=20, blank=True, null=True)
    campus_pincode = models.CharField(max_length=6, blank=True, null=True)
    campus_logo = models.ImageField(upload_to='product', blank=True)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" />' % (self.campus_logo))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.campus_name


class MasterDepartment(models.Model):
    depart_id = models.AutoField(primary_key=True)
    depart_name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.depart_name


class MasterCourse(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.course_name


class Designation(models.Model):
    designation_id = models.AutoField(primary_key=True)
    designation_name = models.CharField(unique=True, max_length=50)
    type = models.IntegerField()

    def __str__(self):
        return self.designation_name


class CampusCourseDepart(models.Model):
    ccd_id = models.AutoField(primary_key=True)
    campus = models.ForeignKey(CampusDetail, on_delete=models.CASCADE)
    course = models.ForeignKey(MasterCourse, on_delete=models.CASCADE)
    department = models.ForeignKey(MasterDepartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.college.college_name + " " + self.course.course_name + " " + self.department.depart_name
