from django.shortcuts import render

# Create your views here.
def main_dashboard(request):
    return render(request, 'main.html', {'active_page': 'panel'})
def create_campaign(request):
    return render(request, 'create_campaign.html', {'active_page': 'create_campaign'})
