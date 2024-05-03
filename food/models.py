from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    email = models.EmailField(default='test@gmail.com')
    
    def __str__(self):
        return f'Name : {self.name} Roll: {self.roll}'
        
        