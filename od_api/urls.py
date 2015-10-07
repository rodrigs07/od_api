from django.conf.urls import patterns, include, url
from userprofile.views import UserViewSet, GroupViewSet
 
urlpatterns = patterns('',
    url(r'^users/$', UserViewSet.as_view()),
    url(r'^groups/$', GroupViewSet.as_view()),
)