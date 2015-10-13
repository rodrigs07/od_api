from django.db import models
from userprofile.models import UserProfile
class Pastors(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    pastor = models.CharField(max_length=50)

