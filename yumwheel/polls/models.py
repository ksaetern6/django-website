from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50, default='Full Name')
    city = models.CharField(max_length=50,default='City')
    description = models.CharField(max_length=200, default='Describe Yourself')
    #created = models.DateTimeField(auto_now_add=True)

    #returns user's name
    def __str__(self):
        return '%s' % (self.user)
#sender = User just created
#**kwargs = key word arguments

def ProfileCreation(sender, **kwargs):
    #if the User has been created, then create the user profile.
    if kwargs['created']:

        user_profile = UserProfile.objects.create(user=kwargs['instance'])

#when user is created run the function "ProfileCreation" and putting
#the variable "sender" == the User object just created.
post_save.connect(ProfileCreation, sender=User)
