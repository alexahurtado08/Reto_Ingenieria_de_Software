from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.conf import settings
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.campaign import Campaign
from .forms import OfertaLaboralForm
from .models import OfertaLaboral

import json
import os

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

def main_dashboard(request):
    return render(request, 'main.html', {'active_page': 'panel'})

def vacante(request):
    context = {'active_page': 'vacante'}
    return render(request, 'vacante.html', context)

def create_campaign(request):
    initial_data = {
        'title': request.GET.get('title', ''),
        'description': request.GET.get('description', '')
    }

    if request.method == 'POST':
        try:
            # Configurar la API de Facebook
            FacebookAdsApi.init(
                app_id=settings.FACEBOOK_APP_ID,
                app_secret=settings.FACEBOOK_APP_SECRET,
                access_token=settings.FACEBOOK_ACCESS_TOKEN,
                api_version='v22.0'
            )
            
            # Crear la campaña
            campaign = Campaign(parent_id=settings.FACEBOOK_AD_ACCOUNT_ID)
            campaign.update({
                'name': request.POST.get('campaign_name'),
                'objective': 'OUTCOME_TRAFFIC',
                'status': 'PAUSED',
                'special_ad_categories': []
            })
            
            campaign.remote_create()
            
            # Mensaje de éxito
            messages.success(request, f'¡Campaña creada exitosamente! ID: {campaign["id"]}')
            return redirect('create_campaign')
            
        except Exception as e:
            # Mensaje de error en caso de fallo
            messages.error(request, f'Error al crear campaña: {str(e)}')
            return redirect('create_campaign')

    # Renderizar el formulario si es GET
    return render(request, 'create_campaign.html', {'initial_data': initial_data})

def vista_ofertas(request):
    ofertas = OfertaLaboral.objects.all()
    print("OFERTAS:", ofertas)
    for o in ofertas:
        print(o.cargo, o.salario, o.ubicacion, o.critica)  # ← imprime info clave
    return render(request, 'vacante.html', {'ofertas': ofertas})





def crear_vacante(request):
    if request.method == 'POST':
        form = OfertaLaboralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacante')  # redirige a la lista de vacantes
    else:
        form = OfertaLaboralForm()

    return render(request, 'crear_vacante.html', {'form': form})
