from django.db import models
from userprofile.models import UserProfile
from coordinators.models import Coordinators

class Shepherds(models.Model):
    shepherds_user_profile = models.ForeignKey(UserProfile)
    coordinators_user_profile = models.ForeignKey(Coordinators)
    

    def __unicode__(self):
    	return unicode(self.shepherds_user_profile)