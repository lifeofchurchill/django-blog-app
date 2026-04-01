from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.contrib.auth.models import User 
from .models import Profile

@receiver(post_save, sender = User) #after a model is saved and after a user is save respectively
def create_profile(sender, instance, created, **kwargs): #"instance" is the data that was saved whiles "created" is a boolean that checks if this is a new user or an updating user
    if created: #only runs when a new user is created
        Profile.objects.create(user=instance) #profile automatically created

@receiver(post_save, sender = User) 
def save_profile(sender, instance, **kwargs): #runs when a user is saved 
    if hasattr(instance, 'profile'):
        instance.profile.save() #saves related profile
