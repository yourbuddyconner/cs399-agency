from django.shortcuts import render
from app.models import Campaign


def home(request):
    return render(request, 'home.html', {
    	'campaigns': Campaign.objects.all()
    })

def campaign_detail(request, id):
    return render(request, 'campaign_detail.html', {
    	'campaign': Campaign.objects.get(pk=int(id))
    })

def merchandise(request):
    return render(request, 'merchandise.html')

def tickets(request):
    return render(request, 'tickets.html')

def schedule(request):
    return render(request, 'schedule.html')