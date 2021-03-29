from django.db import models

# Create your models here.
class username(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    def __str__(self):
        return self.firstname

class password(models.Model):
    pwd=models.CharField(max_length=200)
    cpwd=models.CharField(max_length=200)


