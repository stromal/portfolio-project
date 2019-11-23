from django.db import models
from django.db.models import Model

# Create your models here.
class Blog1(models.Model):
    title_b = models.CharField(max_length=255)
    pub_date_b = models.DateField()
    body_b = models.TextField()
    image_b = models.ImageField(upload_to='images/')

    def summary_b(self):
        return self.body_b[:100]

#add the Blog app to the settings

#create migration

#migrate

#Add to the admin.py the model
