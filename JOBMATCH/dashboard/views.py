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
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import OfertaLaboralForm, CampaniaForm
from django.db.models import Q
from django import forms
from cities_light.models import Country, Region, City
from django.http import JsonResponse
from cities_light.models import Region, City
from .models import Postulacion


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

    ofertas = OfertaLaboral.objects.all()  # <- Obtener todas las ofertas

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

            # 2. Datos del formulario
            nombre = request.POST.get('campaign_name')
            contenido = request.POST.get('ad_content')
            presupuesto = request.POST.get('budget')
            fecha_inicio = request.POST.get('schedule')
            plataformas = request.POST.getlist('platforms')

            # Captura de oferta laboral: primero job_offer, luego fallback a vacante_id
            job_offer_id = request.POST.get('job_offer')
            vacante_id = request.POST.get('vacante_id')
            oferta_id = job_offer_id or vacante_id
            oferta = OfertaLaboral.objects.filter(id=oferta_id).first() if oferta_id else None

            campania = Campania(
                nombre=request.POST.get("campaign_name"),
                contenido=request.POST.get("ad_content"),
                presupuesto=request.POST.get("budget"),
                fecha_inicio=request.POST.get("schedule"),
                OfertaLaboral=oferta,
                estado='activa',  # o el valor que uses por defecto
            )
            campania.save()

            # 4. Asociar plataformas
            for nombre_plataforma in plataformas:
                plataforma = Plataforma.objects.filter(nombre__iexact=nombre_plataforma).first()
                if plataforma:
                    campania.plataformas.add(plataforma)

            messages.success(request, f'Campaña creada exitosamente. ID Facebook: {campaign["id"]}')
            return redirect('dashboard')

        except Exception as e:
            messages.error(request, f'Error al crear campaña: {str(e)}')
            return redirect('create_campaign')

    return render(request, 'create_campaign.html', {
        'initial_data': initial_data,
        'ofertas': ofertas  # <- Enviamos al template
    })
    
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
    campañas = Campania.objects.filter(Q(estado='activa') | Q(estado='pausada'))
    return render(request, 'campania_activas.html', {'campañas': campañas, 'active_page': 'campania'})

def editar_campania(request, pk):
    campania = get_object_or_404(Campania, pk=pk)
    if request.method == 'POST':
        form = CampaniaForm(request.POST, instance=campania)
        if form.is_valid():
            form.save()
            messages.success(request, 'Campaña actualizada exitosamente.')
            return redirect('campania_activas')
    else:
        form = CampaniaForm(instance=campania)
    return render(request, 'editar_campania.html', {'form': form, 'campania': campania})


def pausar_campania(request, pk):
    campania = get_object_or_404(Campania, pk=pk)
    if campania.estado == 'activa':
        campania.estado = 'pausada'
        campania.save()
        messages.info(request, f'Campaña "{campania.nombre}" pausada.')
    return redirect('campania_activas')


def reactivar_campania(request, pk):
    campania = get_object_or_404(Campania, pk=pk)
    if campania.estado == 'pausada':
        campania.estado = 'activa'
        campania.save()
        messages.success(request, f'Campaña "{campania.nombre}" reactivada.')
    return redirect('campania_activas')


def finalizar_campania(request, pk):
    campania = get_object_or_404(Campania, pk=pk)
    if campania.estado != 'finalizada':
        campania.estado = 'finalizada'
        campania.save()
        messages.warning(request, f'Campaña "{campania.nombre}" finalizada.')
    return redirect('campania_activas')


def seleccionar_campania(request):
    campañas_activas = Campania.objects.filter(estado='activa')

    if request.method == 'POST':
        campania_id = request.POST.get('campania_id')
        # Redirigir a la vista del anuncio
        return redirect('vista_anuncio', campania_id=campania_id)

    return render(request, 'seleccionar_campania.html', {'campañas': campañas_activas})



def vista_anuncio(request, campania_id):
    try:
        # Obtener la campaña
        campania = Campania.objects.get(id=campania_id)
        
        # Obtener la oferta laboral asociada a la campaña
        oferta = campania.OfertaLaboral

        # Pasar la información a la plantilla
        return render(request, 'vista_anuncio.html', {'campania': campania, 'oferta': oferta})
    except Campania.DoesNotExist:
        # Manejar el caso donde la campaña no existe
        return render(request, 'error.html', {'message': 'Campaña no encontrada.'})


# Crear el formulario para postulación
from django import forms
from cities_light.models import Country, Region, City

class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postulacion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departamento'].queryset = Region.objects.none()
        self.fields['ciudad'].queryset = City.objects.none()

        if 'pais' in self.data:
            try:
                pais_id = int(self.data.get('pais'))
                self.fields['departamento'].queryset = Region.objects.filter(country_id=pais_id)
            except (ValueError, TypeError):
                pass
        if 'departamento' in self.data:
            try:
                departamento_id = int(self.data.get('departamento'))
                self.fields['ciudad'].queryset = City.objects.filter(region_id=departamento_id)
            except (ValueError, TypeError):
                pass

#Vista para postulación
def postular(request, campania_id):
    if request.method == 'POST':
        form = PostulacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://www.magneto365.com/es')
    else:
        form = PostulacionForm()
    
    return render(request, 'postulacion.html', {'form': form})



def actualizar_departamentos(request):
    pais_id = request.GET.get('pais_id')
    departamentos = Region.objects.filter(country_id=pais_id).values('id', 'name')
    return JsonResponse({'departamentos': list(departamentos)})

def actualizar_ciudades(request):
    departamento_id = request.GET.get('departamento_id')
    ciudades = City.objects.filter(region_id=departamento_id).values('id', 'name')
    return JsonResponse({'ciudades': list(ciudades)})

