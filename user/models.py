from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.sessions.models import Session



class User(AbstractUser):
    phone = models.CharField(verbose_name='phone', max_length=255)
    email = models.CharField(verbose_name='email', max_length=255, unique=True)
    api_key = models.TextField()
    date_registered = models.CharField(verbose_name='date_registered', max_length=100)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'last_name']
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'user'

    def get_username(self):
        return self


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_session'



class State(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'state'


class LocalGovernment(models.Model):
    state_id = models.IntegerField()
    lname = models.CharField(max_length=100)

    class Meta:
        db_table = 'local_government'
