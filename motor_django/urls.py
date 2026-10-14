
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from app_encuestas import views
from rest_framework import routers

enrutador = routers.DefaultRouter()

enrutador.register(r'paises', views.PaisViewSet)
enrutador.register(r'regiones', views.RegionViewSet)
enrutador.register(r'provincias', views.ProvinciaViewSet)
enrutador.register(r'comunas', views.ComunaViewSet)
enrutador.register(r'direcciones', views.DireccionViewSet)
enrutador.register(r'bibliotecas', views.BibliotecaViewSet)
enrutador.register(r'autores', views.AutorViewSet)
enrutador.register(r'generos', views.GeneroViewSet)
enrutador.register(r'subgeneros', views.SubGeneroViewSet)
enrutador.register(r'editoriales', views.EditorialViewSet)
enrutador.register(r'idiomas', views.IdiomaViewSet)
enrutador.register(r'ediciones', views.EdicionViewSet)
enrutador.register(r'libros', views.LibroViewSet)
enrutador.register(r'estados', views.EstadoViewSet)
enrutador.register(r'ubicaciones', views.UbicacionViewSet)
enrutador.register(r'inventarios', views.InventarioViewSet)
enrutador.register(r'usuarios', views.UsuarioViewSet)
enrutador.register(r'prestamos', views.PrestamoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
    path('app_encuestas/', include(enrutador.urls)),

    # URLs de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
]
