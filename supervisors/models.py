from django.db import models
from userprofile.models import UserProfile
from pastors.models import Pastors

class Supervisors(models.Model):
    supervisor_user_profile = models.ForeignKey(UserProfile)
    pastor_user_profile = models.ForeignKey(Pastors)

    def __str__(self):
        return self.supervisor_user_profile