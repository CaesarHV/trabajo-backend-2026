from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from rest_framework import viewsets


from .models import Pais, Region, Provincia, Comuna, Direccion, Biblioteca, Autor, Genero, SubGenero, Editorial, Idioma, Edicion, Libro, Estado, Ubicacion, Inventario, Usuario, Prestamo
from .serializer import PaisSerializer, RegionSerializer, ProvinciaSerializer, ComunaSerializer, DireccionSerializer, BibliotecaSerializer, AutorSerializer, GeneroSerializer, SubGeneroSerializer, EditorialSerializer, IdiomaSerializer, EdicionSerializer, LibroSerializer, EstadoSerializer, UbicacionSerializer, InventarioSerializer, UsuarioSerializer, PrestamoSerializer

# Vista para la página de bienvenida
def bienvenida(request):
    return render(request, 'bienvenida.html')

#Verificar estado de sesión
def vista_protegida(request):
    if not request.user.is_authenticated:
        # Redirecciona a login si el usuario no está autenticado
        return redirect('login')
    return render(request, 'vista_protegida.html')

# Vista de registro de usuario
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form':form})

@login_required
def pagina_inicio(request):
    # Almacenar data en SESSION
    request.session['mensaje_bienvenida'] = '¡Bienvenido!'

    # Obtener data desde SESSION
    mensaje_bienvenida = request.session.get('mensaje_bienvenida')

    # Remover data desde SESSION
    if 'mensaje_bienvenida' in request.session:
        del request.session['mensaje_bienvenida']
        
    return render(request, 'mi_aplicacion/inicio.html', {'message': mensaje_bienvenida})

def logout_view(request):
    # Cierra la sesión del usuario y limpia la data de SESSION
    logout(request)
    # Redirige a la página de inicio de sesión
    return redirect('login')

# API para gestionar los modelos
class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class SubGeneroViewSet(viewsets.ModelViewSet):
    queryset = SubGenero.objects.all()
    serializer_class = SubGeneroSerializer

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer

class EdicionViewSet(viewsets.ModelViewSet):
    queryset = Edicion.objects.all()
    serializer_class = EdicionSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer