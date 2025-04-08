from django.urls import path
from .views import main_dashboard, create_campaign, vacante  # Asegúrate de importar vacante

urlpatterns = [
    path('', main_dashboard, name='dashboard'),  # /dashboard/
    path('create-campaign/', create_campaign, name='create_campaign'),  # /dashboard/create-campaign/
    path('vacante/', vacante, name='vacante'),  # Asegúrate de usar vacante aquí
]
