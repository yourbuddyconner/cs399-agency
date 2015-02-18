from django.shortcuts import render
from app.models import *
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html', {
        'campaigns': Campaign.objects.all()
    })


def campaign_detail(request, id):
    form = Campaign.objects.get(pk=int(id))  # get campaign object
    form = eval(form.formID)                 # turn string to class
    x = {'campaign': Campaign.objects.get(pk=int(id)),'form':form}
    return render(request, 'campaign_detail.html', x)



def merchandise(request):
    return render(request, 'merchandise.html')


def tickets(request):
    return render(request, 'tickets.html')


def schedule(request):
    return render(request, 'schedule.html')