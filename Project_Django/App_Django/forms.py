from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class JeuxForm(ModelForm):
    class Meta:
        model = models.Jeux
        fields = ('nom', 'plateforme', 'date_parution', 'prix','genre', 'resume')
        labels = {
            'nom' : _('nom'),
            'plateforme' : _('plateforme') ,
            'date_parution' : _('date de parution'),
            'prix' : _('prix'),
            'genre' : _('genre'),
            'resume' : _('resume')
        }

class StudiodevForm(ModelForm):
    class Meta:
        model = models.Studiodev
        fields = ('nom', 'franchise')
        labels = {
            'nom' : _('nom'),
            'franchise' : _('franchise')
        }