from django.conf.urls import patterns, include, url

from userprofile.views import UserViewSet,GroupViewSet
from pastors.views import PastorViewSet
from django.contrib import admin
from rest_framework import routers

router_userapp = routers.DefaultRouter()
router_userapp.register(r'users', UserViewSet)
router_userapp.register(r'groups',GroupViewSet)


#SUGESTION: Each app work with our own router, because it looks the correct mode for work with routers
router_pastors = routers.DefaultRouter()
router_pastors.register(r'pastors', PastorViewSet)


urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router_userapp.urls)),
    url(r'^', include(router_pastors.urls)),
)