from django.contrib import admin
from django.urls import path, include
from app_encuestas import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'paises', views.PaisViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
    path('api/', include(router.urls)),
]