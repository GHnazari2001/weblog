from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
  
    age = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(
        upload_to='photo/profile/%Y/%m/%d/', null= True , blank= True)
    about = models.CharField(max_length=255, null=True ,blank= True)
    
    instagram = models.CharField(max_length=150 ,null=True ,blank= True ,verbose_name='Instagram Id without @' )
    telegram = models.CharField(max_length=150 ,null=True ,blank= True ,verbose_name='Telegram Id without @' )
    linkedin = models.CharField(max_length=150 ,null=True ,blank= True ,verbose_name='linkedin Id without @' )
    facebook = models.URLField(max_length=150 ,null=True ,blank= True ,verbose_name='facebook link ' )

    