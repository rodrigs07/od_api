from django.db import models
from userprofile.models import UserProfile
from supervisors.models import Supervisors

class Coordinators(models.Model):
    coordinator_user_profile = models.ForeignKey(UserProfile)
    supervisor_user_profile = models.ForeignKey(Supervisors)

    def __unicode__(self):
    	return unicode(self.coordinator_user_profile)