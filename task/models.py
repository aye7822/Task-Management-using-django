from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    isCompleted=models.BooleanField(default=False)
    assignDate=models.DateField()
    category=models.ManyToManyField('category.Category')
    
    def __str__(self):
        return self.title