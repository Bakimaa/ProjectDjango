from django.shortcuts import render, HttpResponseRedirect
from .forms import JeuxForm
from . import models

def traitement(request):
    if request.method == "POST":
        form = JeuxForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/App_Django/")
            #return render(request,"App_Django/affiche.html",{"Jeux" : Jeux})
        else:
            return render(request,"App_Django/ajout.html",{"form": form})

def ajout(request):
    form_vide = JeuxForm()
    return render(request, "App_Django/ajout.html", {"form": form_vide})

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
    if request.method == "POST":
        form = JeuxForm(request.POST)
        if form.is_valid():
            jeux = form.save(commit = False)
            jeux.id = id
            jeux.save()
            return HttpResponseRedirect("/App_Django/")
        else:
            return render(request, "App_Django/ajout.html", {"form": form, "id": id})

def delete(request, id):
     jeux = models.Jeux.objects.get(pk=id)
     jeux.delete()
     return HttpResponseRedirect("/App_Django/")