from django.apps import AppConfig


class UserAviationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User_Aviation'
    
    
    def ready(self):
       import User_Aviation.signals
