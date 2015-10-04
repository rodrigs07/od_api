from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'membro', views.MembroViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
