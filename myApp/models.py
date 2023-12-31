from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " is from " + self.city +"."


class Video_1(models.Model):
    name = models.CharField(max_length=100)
    vid = models.FileField(blank=True, upload_to="uploads/")

    def __str__(self):
        return self.name
