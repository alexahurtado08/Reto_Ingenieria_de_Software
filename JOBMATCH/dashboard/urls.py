from django.urls import path
from . import views
from .views import main_dashboard, create_campaign, vacante, vista_ofertas,crear_vacante, login_view, campania_activas
urlpatterns = [
    path('', main_dashboard, name='dashboard'),
    path('create-campaign/', create_campaign, name='create_campaign'),
    path('ofertas/', vista_ofertas, name='ofertas'),
    path('vacante/', vista_ofertas, name='vacante'),
    path('crear-vacante/', crear_vacante, name='crear_vacante'),
    path('login/', login_view, name='login'),
    path('campanias-activas/', campania_activas, name='campania_activas'),
     path('campania/<int:pk>/editar/', views.editar_campania, name='editar_campania'),
    path('campania/<int:pk>/pausar/', views.pausar_campania, name='pausar_campania'),
    path('campania/<int:pk>/reactivar/', views.reactivar_campania, name='reactivar_campania'),
    path('campania/<int:pk>/finalizar/', views.finalizar_campania, name='finalizar_campania'),
    path('seleccionar-campania/', views.seleccionar_campania, name='seleccionar_campania'),
    path('ver-anuncio/<int:campania_id>/', views.vista_anuncio, name='vista_anuncio'),
    path('postular/<int:campania_id>/', views.postular, name='postular'),






]

