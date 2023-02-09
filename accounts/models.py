from django.db import models
from django.conf import settings 
# Create your models here.
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save



class Profile(models.Model) : 

    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profiles')



@receiver(post_save ,sender = get_user_model())
def create_profile(sender ,instance ,created ,**kwargs) : 
    try  : 
        if created : 
            Profile.objects.create(user= instance)
    except Exception as e :
        print(e)




