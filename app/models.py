from django.db import models
from django.urls import reverse
# Create your models here.
class school(models.Model):
    sname=models.CharField(max_length=100)
    sprinpal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.sname
    

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})



class student(models.Model):
    stname= models.CharField(max_length=100)
    stage = models.IntegerField()
    sname = models.ForeignKey(school, on_delete=models.CASCADE,related_name='student')

    def __str__(self) -> str:
        return self.stname
    