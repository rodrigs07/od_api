from django.conf.urls import patterns, include, url

from userprofile.views import UserViewSet,GroupViewSet
from pastors.views import PastorViewSet
from supervisors.views import SupervisorsViwesSets
from django.contrib import admin
from rest_framework import routers

router_userapp = routers.DefaultRouter()
router_userapp.register(r'users', UserViewSet)
router_userapp.register(r'groups',GroupViewSet)


router_pastors = routers.DefaultRouter()
router_pastors.register(r'pastors', PastorViewSet)

router_supervisors = routers.DefaultRouter()
router_supervisors.register(r'supervisors', SupervisorsViwesSets)

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router_userapp.urls)),
    url(r'^', include(router_pastors.urls)),
    url(r'^', include(router_supervisors.urls)),
)