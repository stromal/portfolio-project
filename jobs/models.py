from django.db import models

# Create your models here.
class Job1(models.Model): #saving down data to database model(this file).Model(file type)
    #https://docs.djangoproject.com/en/2.2/ref/models/fields/
    image = models.ImageField(upload_to='images/') #autorename same nemed images
    summary = models.CharField(max_length=200)
