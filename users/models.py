from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
# Create your models here.

class User(AbstractUser):
    is_tm=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

    def __str__(self) :
        return str(self.username)
        
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Tm(models.Model):
    user=models.OneToOneField(User, related_name="tm", on_delete=models.CASCADE)
    phone=models.CharField(max_length=12, null=True, blank=True)
    skills=models.CharField(max_length=100, null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    portofolio=models.URLField(null=True)

    def __str__(self):
        return str(self.user.username)




class Student(models.Model):
    user=models.OneToOneField(User, related_name="student", on_delete=models.CASCADE)
    course=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.course)



class Shedule(models.Model):
    day = models.CharField(max_length=250)
    details = models.TextField()
    time = models.CharField(max_length=350)

    def __str__(self):
        return self.day


class Session(models.Model):
    title = models.CharField(max_length=122)
    description = models.TextField()
    date= models.DateTimeField()
    time= models.CharField(max_length=33)
    link= models.URLField()








