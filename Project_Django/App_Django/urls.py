from django.urls import path

from . import views

urlpatterns = [
    path('ajout/', views.ajout),
    path('affiche/<int:id>/', views.affiche),
    path('traitement/', views.traitement),
    path('', views.index),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
#pages pour les Studios de développement de jeu vidéo
    path('ajoutstudiodev/', Studiodev_views.ajout),
    path('affichestudiodev/<int:id>/', Studiodev_views.affiche),
    path('traitementstudiodev/', Studiodev_views.traitement),
    path('indexstudiodev/', Studiodev_views.index),
    path('updatestudiodev/<int:id>/', Studiodev_views.update),
    path('updatetraitementstudiodev/<int:id>/', Studiodev_views.updatetraitement),
    path('deletestudiodev/<int:id>/', Studiodev_views.delete),
]
