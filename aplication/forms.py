from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioInstrumentosPorMarca(forms.Form):
    instrumentos = (
        (1, "Guitarra"),
        (2, "Bajo"),
        (3, "Teclado"),
    )
    
    marcas = (
        (1, "Ibanez"),
        (2, "Gibson"),
        (3, "Fender"),
        (4, "Casio"),
        (5, "Yamaha"),
    )
        
    tipo = forms.ChoiceField(label="Instrumento", choices=instrumentos, required=True)
    marca = forms.ChoiceField(label="Marca", choices=marcas, required=True)

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
            help_texts = {k:"" for k in fields}  

class FormularioEditarUsuario(UserCreationForm):
    email = forms.EmailField(label="Cambiar Email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name'] 
        help_texts = { k:"" for k in fields}

class FormularioAvatarUsuario(forms.Form):
    image = forms.ImageField(required=True)   