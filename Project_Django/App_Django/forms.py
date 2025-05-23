from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class JeuxForm(ModelForm):
    class Meta:
        model = models.Jeux
        fields = ('nom', 'plateforme', 'date_parution', 'prix','genre', 'resume')
        labels = {
            'nom' : _('Nom'),
            'plateforme' : _('Plateforme') ,
            'date_parution' : _('Date de parution'),
            'prix' : _('Prix'),
            'genre' : _('Genre'),
            'resume' : _('Résumé')
        }

class StudiodevForm(ModelForm):
    class Meta:
        model = models.Studiodev
        fields = ('nom', 'franchise')
        labels = {
            'nom' : _('nom'),
            'franchise' : _('franchise')
        }