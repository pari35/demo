# import email
# from email.policy import default
# from ftplib import MAXLINE
# from pyexpat import model
from random import Random
from django.db import models
from sqlalchemy import null
import random

# Create your models here.
#models for add project
class user1(models.Model):
    pname = models.CharField(max_length=20, default="")
    members=models.CharField(max_length=20, default="")
    ptech =(models.CharField(max_length=30))
    deadline=models.CharField(max_length=20, default="")
    vcont=models.CharField(max_length=20, default="")
    cicd=models.CharField(max_length=20, default="")
def __str__(self):
        return str(self.pname)

#model for add technology
class addtech(models.Model):
    techname=models.CharField(max_length=20,default="")

#model for add_git_platform
class addgit(models.Model):
    git_id=models.AutoField(primary_key=True),
    gitplat=models.CharField(max_length=20,default="")
    def __str__(self):
            return str(self.gitplat)

# class Projects(models.Model):
#     """project model"""
#     project_id                = models.AutoField
#     project_name              = models.CharField(max_length=30, null=True)
#     technologies_used         = models.CharField(max_length=20)#models.ManyToManyField(Technologies)
#     git_platform              = #models.ForeignKey(GitPlatforms, null= True, on_delete= models.CASCADE,
#                                     related_name="project_version_control_platforms",
#                                     related_query_name="project_version_control_platforms",)
#     project_deadline          = models.IntegerField(default=60, validators=[
#                                     MaxValueValidator(100),
#                                     MinValueValidator(60)
#                                 ])   # in days
#     project_members           = models.ManyToManyField(Employees)
#     have_cicd                 = models.BooleanField(default=False)

#     class Meta:
#         db_table = "projects"

#     def __str__(self):
#         return str(self.project_name)

class projects(models.Model):
    """Project  model"""
    project_id          = models.AutoField
    project_name         =models.CharField(max_length=30, null=True)
    technologies_used    =models.CharField(max_length=30, null=True)
    git_platform          =models.CharField(max_length=30, null=True)
    project_deadline     = models.IntegerField(default=60)
                                #   MaxValueValidator(100),
                                #   MinValueValidator(60) ])