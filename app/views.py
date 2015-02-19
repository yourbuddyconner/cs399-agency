from django.shortcuts import render
from app.models import *
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html', {
        'campaigns': Campaign.objects.all(),
        'navoptions': [('About', '#about'), ('Campaigns', '#campaigns'), ('Contact', '#contact')]
    })


def campaign_detail(request, id):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            template_params = {
                'campaign': Campaign.objects.get(pk=int(id)),
                'form':form,
                'name':name,
                'navoptions': [('Go Home', '/home/')]
            }
            return render(request, 'thank_you.html', template_params)
    else:
        form = CampaignForm()

    return render(request, 'campaign_detail.html', {
        'campaign': Campaign.objects.get(pk=int(id)),
        'form':form,
        'navoptions': [('Sign Up', '#sign-up')]
    })

def thank_you(request):
    return render(request, 'thank_you.html', {
        'navoptions': [('Go Home', '/home/')]
    })
