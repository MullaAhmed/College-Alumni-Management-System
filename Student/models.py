from django.db import models

# Create your models here.
class ChatBox(models.Model):
    name=models.CharField(max_length=200)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.name,self.body)

class Profile(models.Model):
    about_me=models.CharField(max_length=200)
    currently_working=models.CharField(max_length=200)
    previously_working=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    college=models.CharField(max_length=200)
    degree=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    email=models.EmailField(max_length=50)
    graduation_year=models.IntegerField()
    number=models.IntegerField()

    def __str__(self):
        return '%s -%s - %s - %s' % (self.first_name,self.last_name,self.college,self.graduation_year)
    