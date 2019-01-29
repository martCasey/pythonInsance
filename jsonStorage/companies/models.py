from django.db import models

# Create your models here.
class Organisation(models.Model):
	name = models.StringField()
	address = models.StringField()
	type = models.StringField()
