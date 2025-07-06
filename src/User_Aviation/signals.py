from django.db.models.signals import post_save
from .models import *
from django.contrib.auth.models import Group






def create_Client_Profile(sender , instance ,created , **kwargs):
    
     if created:
         group = Group.objects.get(name="clients")
         instance.groups.add(group)

         ClientAv.objects.create(
             user = instance,
             user_nameAV = instance.username,
             email = instance.email,
         )

         print('Customer profile created ! ')

post_save.connect(create_Client_Profile, sender=User)