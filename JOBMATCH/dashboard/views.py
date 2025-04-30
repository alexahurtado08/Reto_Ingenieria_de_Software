from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.conf import settings
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.campaign import Campaign
from .forms import OfertaLaboralForm
from .models import OfertaLaboral
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import Campania
from .models import Plataforma



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
            # 1. Crear campaña en Facebook
            FacebookAdsApi.init(
                app_id=settings.FACEBOOK_APP_ID,
                app_secret=settings.FACEBOOK_APP_SECRET,
                access_token=settings.FACEBOOK_ACCESS_TOKEN,
                api_version='v22.0'
            )
            campaign = Campaign(parent_id=settings.FACEBOOK_AD_ACCOUNT_ID)
            campaign.update({
                'name': request.POST.get('campaign_name'),
                'objective': 'OUTCOME_TRAFFIC',
                'status': 'PAUSED',
                'special_ad_categories': []
            })
            campaign.remote_create()

            # 2. Guardar campaña en base de datos
            nombre = request.POST.get('campaign_name')
            contenido = request.POST.get('ad_content')
            presupuesto = request.POST.get('budget')
            fecha_inicio = request.POST.get('schedule')
            plataformas = request.POST.getlist('platforms')
            vacante_id = request.POST.get('vacante_id')  # si pasas la vacante como hidden input

            campania = Campania.objects.create(
                nombre=nombre,
                contenido=contenido,
                presupuesto=presupuesto,
                fecha_inicio=fecha_inicio,
                OfertaLaboral_id=vacante_id if vacante_id else None,
                id_facebook=campaign['id'],
                estado='activa'  # o el estado que desees por defecto
            )

            for nombre_plataforma in plataformas:
                plataforma = Plataforma.objects.filter(nombre__iexact=nombre_plataforma).first()
                if plataforma:
                    campania.plataformas.add(plataforma)

            messages.success(request, f'Campaña creada exitosamente. ID Facebook: {campaign["id"]}')
            return redirect('dashboard')

        except Exception as e:
            messages.error(request, f'Error al crear campaña: {str(e)}')
            return redirect('create_campaign')

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

def login_view(request):
    return render(request, 'login.html', {'active_page': 'login'})


def campania_activas(request):
    campañas = Campania.objects.filter(estado='activa')
    return render(request, 'campania_activas.html', {'campañas': campañas, 'active_page': 'campania'})





