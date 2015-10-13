from django.conf.urls import patterns, include, url
from userprofile.views import UserViewSet, GroupViewSet
from pastors.views import PastorViews
 
urlpatterns = patterns('',
    url(r'^users/$', UserViewSet.as_view()),
    url(r'^groups/$', GroupViewSet.as_view()),
    url(r'^pastors/$', PastorViews.as_view()),
)