from django.db import models

# Create your models here.
class job1(models.Model): #saving down data to database model(this file).Model(file type)
    #https://docs.djangoproject.com/en/2.2/ref/models/fields/
    image1 = models.ImageField(upload_to='images/') #autorename same nemed images
    summary1 = models.CharField(max_length=200)
