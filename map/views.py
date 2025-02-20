from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Situation


# Create your views here.


class SituationView(CreateView):
    model = Situation
    fields = ['address']
    template_name = 'Immo/post_detail.html'
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['acces_token'] = 'pk.eyJ1IjoieW91bmVzMngxOTk5IiwiYSI6ImNreDloMXNsdDA3ajYyb213OGd6NWZzNTgifQ.BJWq3YKGRvd0iaZaofY_7Q' #jeton d'accès.
        context['map'] = Situation.objects.all()
        return context


