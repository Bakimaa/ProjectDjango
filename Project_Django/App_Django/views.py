from django.shortcuts import render, HttpResponseRedirect
from .forms import JeuxForm
from . import models

def traitement(request, id):
    studiodev = models.Studiodev.objects.get(pk=id)
    form = JeuxForm(request.POST)
    if form.is_valid():
        jeu = form.save(commit=False)
        jeu.studiodev = studiodev
        jeu.studiodev_id = id
        jeu.save()
        return HttpResponseRedirect("/App_Django/index")
    else:
        return render(request,"App_Django/ajout.html",{"form": form, "id":id})

def ajout(request, id):
    form_vide = JeuxForm()
    return render(request, "App_Django/ajout.html", {"form": form_vide, "id": id})

def affiche(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    return render(request,"App_Django/affiche.html", {"Jeux": jeux})


def index(request):
    liste = list(models.Jeux.objects.all())
    return render(request,"App_Django/index.html",{"liste" : liste})

def update(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    form = JeuxForm(jeux.dico())
    return render(request, "App_Django/ajout.html",{"form" : form, "id" : id})

def updatetraitement(request, id):
    form = JeuxForm(request.POST)
    return render(request, "App_Django/ajout.html", {"form": form, "id": id})

def delete(request, id):
     jeux = models.Jeux.objects.get(pk=id)
     jeux.delete()
     return HttpResponseRedirect("/App_Django/index")