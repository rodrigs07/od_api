from django.conf.urls import patterns, include, url
from userprofile import views
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
 
urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls))
)