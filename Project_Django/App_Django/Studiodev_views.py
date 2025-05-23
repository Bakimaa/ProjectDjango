from django.shortcuts import render, HttpResponseRedirect
from .forms import StudiodevForm
from . import models

def traitementstudiodev(request):
    if request.method == "POST":
        form = StudiodevForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/App_Django/")
        else:
            return render(request,"Studiodev/ajout.html",{"form": form})

def ajoutstudiodev(request):
    form_vide = StudiodevForm()
    return render(request, "Studiodev/ajout.html", {"form": form_vide})

def affichestudiodev(request, id):
    Studiodev = models.Studiodev.objects.get(pk=id)
    liste = models.Jeux.objects.filter(studiodev_id=id)
    return render(request,"Studiodev/affiche.html", {"Studiodev": Studiodev, "liste": liste})


def indexstudiodev(request):
    liste = list(models.Studiodev.objects.all())
    return render(request,"Studiodev/index.html",{"liste" : liste})

def updatestudiodev(request, id):
    Studiodev = models.Studiodev.objects.get(pk=id)
    form = StudiodevForm(Studiodev.dico())
    return render(request, "Studiodev/ajout.html",{"form" : form, "id" : id})

def updatetraitementstudiodev(request, id):
    if request.method == "POST":
        form = StudiodevForm(request.POST)
        if form.is_valid():
            Studiodev = form.save(commit = False)
            Studiodev.id = id
            Studiodev.save()
            return HttpResponseRedirect("/App_Django/")
        else:
            return render(request, "Studiodev/ajout.html", {"form": form, "id": id})

def deletestudiodev(request, id):
     Studiodev = models.Studiodev.objects.get(pk=id)
     Studiodev.delete()
     return HttpResponseRedirect("/App_Django/")
