from django.db import models
from userprofile.models import UserProfile
class Pastors(models.Model):
    pastor_user_profile = models.ForeignKey(UserProfile)
    state= models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return ("%s" %self.pastor_user_profile)