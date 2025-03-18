from django.urls import path
from .views import main_dashboard, create_campaign

urlpatterns = [
    path('', main_dashboard, name='dashboard'),  # /dashboard/
    path('create-campaign/', create_campaign, name='create_campaign'),  # /dashboard/create-campaign/
]