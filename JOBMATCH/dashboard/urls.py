from django.urls import path
from .views import main_dashboard, create_campaign, vacante, vista_ofertas,crear_vacante, login_view, campania_activas
urlpatterns = [
    path('', main_dashboard, name='dashboard'),
    path('create-campaign/', create_campaign, name='create_campaign'),
    path('ofertas/', vista_ofertas, name='ofertas'),
    path('vacante/', vista_ofertas, name='vacante'),
    path('crear-vacante/', crear_vacante, name='crear_vacante'),
    path('login/', login_view, name='login'),
    path('campanias-activas/', campania_activas, name='campania_activas'),




]

