from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_dashboard, name='dashboard'),
    path('create-campaign/', views.create_campaign, name='create_campaign'),
    path('ofertas/', views.vista_ofertas, name='ofertas'),
    path('vacante/', views.vacante, name='vacante'),
    path('crear-vacante/', views.crear_vacante, name='crear_vacante'),

    # Login / Registro
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),

    # Campañas
    path('campanias-activas/', views.campania_activas, name='campania_activas'),
    path('campania/<int:pk>/editar/', views.editar_campania, name='editar_campania'),
    path('campania/<int:pk>/pausar/', views.pausar_campania, name='pausar_campania'),
    path('campania/<int:pk>/reactivar/', views.reactivar_campania, name='reactivar_campania'),
    path('campania/<int:pk>/finalizar/', views.finalizar_campania, name='finalizar_campania'),
    path('seleccionar-campania/', views.seleccionar_campania, name='seleccionar_campania'),

    # Anuncios y postulación
    path('ver-anuncio/<int:campania_id>/', views.vista_anuncio, name='vista_anuncio'),
    path('postular/<int:campania_id>/', views.postular, name='postular'),

    # AJAX para departamentos/ciudades
    path('actualizar-departamentos/', views.actualizar_departamentos, name='actualizar_departamentos'),
    path('actualizar-ciudades/', views.actualizar_ciudades, name='actualizar_ciudades'),
]
