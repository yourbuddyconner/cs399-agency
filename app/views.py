from django.shortcuts import render
from app.models import *
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html', {
        'campaigns': Campaign.objects.all()
    })


def campaign_detail(request, id):
    if request.POST:
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            template_params = {'campaign': Campaign.objects.get(pk=int(id)),'form':form,'name':name}
            return render(request, 'thank_you.html', template_params)
    else:
        form = CampaignForm()

    template_params = {'campaign': Campaign.objects.get(pk=int(id)),'form':form}
    return render(request, 'campaign_detail.html', template_params)

def thank_you(request):
    return render(request, 'thank_you.html')
	

def merchandise(request):
    return render(request, 'merchandise.html')


def tickets(request):
    return render(request, 'tickets.html')


def schedule(request):
    return render(request, 'schedule.html')