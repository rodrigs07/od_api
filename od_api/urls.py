from django.conf.urls import patterns, include, url

from userprofile.views import UserViewSet,GroupViewSet
from pastors.views import PastorViewSet
from supervisors.views import SupervisorsViwesSets
from coordinators.views import CoordinatorsViwesSets
from shepherds.views import ShepherdsViwesSets
from django.contrib import admin
from rest_framework import routers

router_userapp = routers.DefaultRouter()
router_userapp.register(r'users', UserViewSet)
router_userapp.register(r'groups',GroupViewSet)


router_pastors = routers.DefaultRouter()
router_pastors.register(r'pastors', PastorViewSet)

router_supervisors = routers.DefaultRouter()
router_supervisors.register(r'supervisors', SupervisorsViwesSets)

router_coordinators = routers.DefaultRouter()
router_coordinators.register(r'coordinators', CoordinatorsViwesSets)

router_shepherds = routers.DefaultRouter()
router_shepherds.register(r'shepherds', ShepherdsViwesSets)

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router_userapp.urls)),
    url(r'^', include(router_pastors.urls)),
    url(r'^', include(router_supervisors.urls)),
    url(r'^', include(router_coordinators.urls)),
    url(r'^', include(router_shepherds.urls)),
)