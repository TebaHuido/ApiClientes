from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

def profile_default():
	return Profile.objects.get(pname='student').pk

def permission_default():

	return Permission.objects.get(permname='view').pk

class Permission(models.Model):
	description=models.CharField(max_length=500)
	permname=models.CharField(max_length=200)
	def __unicode__(self):
		return self.permname

class Profile(models.Model):
	pname=models.CharField(max_length=200)
	permission=models.ManyToManyField(Permission)
	def __unicode__(self):
		return self.pname

class User(models.Model):
	uname=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	mail=models.CharField(max_length=200)
	rut=models.CharField(max_length=11)
	profile=models.ManyToManyField(Profile)
	def __unicode__(self):
		return self.uname