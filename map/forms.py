from django import forms

from map.models import Situation


class SituationtForm(forms.ModelForm):
    class Meta:
        model = Situation
        fields = ['address', 'longitude', 'latitude']
