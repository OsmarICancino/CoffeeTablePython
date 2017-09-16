from django.db import models

# Create your models here.
class User(models.Model):
	
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	country = models.CharField(max_length=200)
	verified = models.BooleanField()
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

	#def __init__(self, arg):
	#	super(User, self).__init__()
	#	self.arg = arg

	def __srt__(self):
		return self.username
		