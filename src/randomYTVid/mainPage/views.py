from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mainPage.models import Videos
import random
import webbrowser

# Create your views here.

def randomLink():
    poopyVids = Videos.create()
    for x in poopyVids:
        x.save()

    randomId = random.randint(1, 900)
    videoStringList = list(Videos.objects.all())
    videoString = str(videoStringList[randomId])
    finalVideoLink = "http://www.youtube.com/v/"+videoString+"?version=3"

    return finalVideoLink

def mainPage(request):
    finalVideoLink = randomLink()

    template = loader.get_template('mainPage.html')
    context = {
            'videoLink': finalVideoLink,
            }

    if(request.GET.get("loadVid")):
        finalVideoLink = randomLink()
        context = {
                'videoLink': finalVideoLink,
                }
        
        return HttpResponse(template.render(context, request))


    return HttpResponse(template.render(context, request))



















