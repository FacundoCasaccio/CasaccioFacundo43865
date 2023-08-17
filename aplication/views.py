from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "aplication/index.html")

# ____________Class based view: Instrumento
class InstrumentoList(LoginRequiredMixin, ListView):
    model = Instrumento

class InstrumentoCreate(LoginRequiredMixin, CreateView):
    model = Instrumento
    fields = ['tipo', 'marca', 'modelo', 'precio']
    success_url = reverse_lazy('instrumentos')

class InstrumentoDetail(LoginRequiredMixin, DetailView):
    model = Instrumento

class InstrumentoUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    fields =['tipo', 'marca', 'modelo', 'precio']
    success_url = reverse_lazy('instrumentos')    

class InstrumentoDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('instrumentos')  

# ____________Class based view: Disco
class DiscoList(LoginRequiredMixin, ListView):
    model = Disco

class DiscoCreate(LoginRequiredMixin, CreateView):
    model = Disco
    fields = ['artista', 'album', 'precio']
    success_url = reverse_lazy('discos')

class DiscoDetail(LoginRequiredMixin, DetailView):
    model = Disco

class DiscoUpdate(LoginRequiredMixin, UpdateView):
    model = Disco
    fields = ['artista', 'album', 'precio']
    success_url = reverse_lazy('discos')    

class DiscoDelete(LoginRequiredMixin, DeleteView):
    model = Disco
    success_url = reverse_lazy('discos')  

# ____________Class based view: Remera
class RemeraList(LoginRequiredMixin, ListView):
    model = Remera

class RemeraCreate(LoginRequiredMixin, CreateView):
    model = Remera
    fields = ['modelo', 'color', 'precio']
    success_url = reverse_lazy('remeras')

class RemeraDetail(LoginRequiredMixin, DetailView):
    model = Remera

class RemeraUpdate(LoginRequiredMixin, UpdateView):
    model = Remera
    fields = ['modelo', 'color', 'precio']
    success_url = reverse_lazy('remeras')    

class RemeraDelete(LoginRequiredMixin, DeleteView):
    model = Remera
    success_url = reverse_lazy('remeras')  

# ____________Formulario de busqueda de instrumentos
@login_required
def busquedaForm(request):
    if request.method == "GET":   
        formulario = FormularioInstrumentosPorMarca(request.GET)
        if formulario.is_valid():
            # Opciones de los select
            tipo_instrumento = formulario.cleaned_data.get('tipo')
            marca_instrumento = formulario.cleaned_data.get('marca')

            # Labels de los select
            tipo_instrumento_label = formulario.fields['tipo'].choices[int(tipo_instrumento) - 1][1]
            marca_instrumento_label = formulario.fields['marca'].choices[int(marca_instrumento) - 1][1]
            
            instrumentos = Instrumento.objects.filter(tipo__icontains=tipo_instrumento_label, 
                                                      marca__icontains=marca_instrumento_label)
            

            return render(request, 
                      "aplication/resultados_busqueda.html", 
                      {"tipo": tipo_instrumento_label, "marca":marca_instrumento_label, "instrumentos":instrumentos,
                      })
    else:
        formulario = FormularioInstrumentosPorMarca()

    return render(request, "aplication/buscar_instrumento.html", {"form":formulario})

# ____________Login de usuarios
def login_request(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            credenciales = authenticate(username=username, password=password)

            if credenciales is not None:
                login(request, credenciales)
                return render(request, "aplication/index.html", {"login_error_message": f"Has iniciado sesion como {username}"})
            else:
                return render(request, "aplication/login.html", {"form":login_form, "login_error_message": "Hubo un error en los datos ingresados"})
        else:    
            return render(request, "aplication/login.html", {"form":login_form, "login_error_message": "Hubo un error en los datos ingresados"})

    login_form = AuthenticationForm()

    return render(request, "aplication/login.html", {"form":login_form})    

# ____________Registro de usuarios
def register(request):
    if request.method == 'POST':
        register_form = FormularioRegistro(request.POST) 
        if register_form.is_valid():  
            username = register_form.cleaned_data.get('username')
            register_form.save()
            return render(request, "aplication/index.html", {"success_message":"Usuario Creado"})        
    else:
        register_form = FormularioRegistro() 

    return render(request, "aplication/registro.html", {"form": register_form})  

# ____________Modificar usuario
@login_required
def editarPerfil(request):
    user = request.user
    if request.method == "POST":
        edit_form = FormularioEditarUsuario(request.POST)
        if edit_form.is_valid():
            user.email = edit_form.cleaned_data.get('email')
            user.password1 = edit_form.cleaned_data.get('password1')
            user.password2 = edit_form.cleaned_data.get('password2')
            user.first_name = edit_form.cleaned_data.get('first_name')
            user.last_name = edit_form.cleaned_data.get('last_name')
            user.save()
            return render(request, "aplication/index.html", {'mensaje': f"Datos modificados con exito"})
        else:
            return render(request, "aplication/edit_user.html", {'form': edit_form})
    else:
        edit_form = FormularioEditarUsuario(instance=user)
    return render(request, "aplication/edit_user.html", {'form': edit_form, 'usuario':user.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        avatar_form = FormularioAvatarUsuario(request.POST, request.FILES)
        if avatar_form.is_valid():
            user = User.objects.get(username=request.user)

            # Limpiar avatar existente
            current_avatar = UserAvatar.objects.filter(user=user)
            if len(current_avatar) > 0:
                current_avatar[0].delete()

            # Guardar nuevo
            avatar = UserAvatar(user=user, imagen=avatar_form.cleaned_data['imagen'])
            avatar.save()

            # Guardar direccion de avatar
            imagen = UserAvatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplication/index.html")
    else:
        avatar_form = FormularioAvatarUsuario()
    return render(request, "aplication/add_avatar.html", {'form': avatar_form})