from django.db import models

class Details(models.Model):
    name=models.CharField(max_length=100)
    age=models.DateField()
    gender=models.CharField(max_length=50)
    degree=models.TextField(max_length=50)
    address=models.TextField(max_length=255)
    image=models.ImageField (upload_to='picture/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return self.name
