from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vendor_profile')
    address = models.CharField(max_length=50)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
