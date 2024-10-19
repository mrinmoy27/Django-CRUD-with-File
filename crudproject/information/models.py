from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='upload/', default='img-1.jpg')
    password = models.CharField(max_length=25)


    def __str__(self):
        return self.name
