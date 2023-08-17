from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # ________Direccion pagina base
    path('', index, name="inicio"),

    # ________Direcciones de instrumentos
    path('instrumentos/', InstrumentoList.as_view(), name="instrumentos"),
    path('cargar_instrumentos/', InstrumentoCreate.as_view(), name="create_instrumento"),
    path('detalle_instrumento/<int:pk>/', InstrumentoDetail.as_view(), name="detail_instrumento"),
    path('modificar_instrumento/<int:pk>/', InstrumentoUpdate.as_view(), name="update_instrumento"),
    path('eliminar_instrumento/<int:pk>/', InstrumentoDelete.as_view(), name="delete_instrumento"),

    # ________Direcciones de discos
    path('discos/', DiscoList.as_view(), name="discos"),
    path('cargar_discos/', DiscoCreate.as_view(), name="create_disco"),
    path('detalle_disco/<int:pk>/', DiscoDetail.as_view(), name="detail_disco"),
    path('modificar_disco/<int:pk>/', DiscoUpdate.as_view(), name="update_disco"),
    path('eliminar_disco/<int:pk>/', DiscoDelete.as_view(), name="delete_disco"),

    # ________Direcciones de remeras
    path('remeras/', RemeraList.as_view(), name="remeras"),
    path('cargar_remeras/', RemeraCreate.as_view(), name="create_remera"),
    path('detalle_remera/<int:pk>/', RemeraDetail.as_view(), name="detail_remera"),
    path('modificar_remera/<int:pk>/', RemeraUpdate.as_view(), name="update_remera"),
    path('eliminar_remera/<int:pk>/', RemeraDelete.as_view(), name="delete_remera"),

    # ________Direccion formulario de busqueda
    path('buscar_instrumentos/', busquedaForm, name="buscar_instrumentos"),

    # ________Direcciones autenticacion
    path('iniciar_sesion/', login_request, name="login"),
    path('cerrar_sesion/', LogoutView.as_view(template_name="aplication/logout.html"), name="logout"),
    path('registrarse/', register, name="register"),

    # ________Direcciones autenticacion
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]
