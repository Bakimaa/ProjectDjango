from django.urls import path

from . import views, Studiodev_views

urlpatterns = [
    path('ajout/<int:id>/', views.ajout),
    path('affiche/<int:id>/', views.affiche),
    path('traitement/<int:id>/', views.traitement),
    path('index', views.index),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
#pages pour les Studios de développement de jeu vidéo
    path('ajoutstudiodev/', Studiodev_views.ajoutstudiodev),
    path('affichestudiodev/<int:id>/', Studiodev_views.affichestudiodev),
    path('traitementstudiodev/', Studiodev_views.traitementstudiodev),
    path('', Studiodev_views.indexstudiodev),
    path('updatestudiodev/<int:id>/', Studiodev_views.updatestudiodev),
    path('updatetraitementstudiodev/<int:id>/', Studiodev_views.updatetraitementstudiodev),
    path('deletestudiodev/<int:id>/', Studiodev_views.deletestudiodev),
]
