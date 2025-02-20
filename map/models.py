import geocoder
from django.db import models

# Create your models here.


token = 'pk.eyJ1IjoieW91bmVzMngxOTk5IiwiYSI6ImNreDloMXNsdDA3ajYyb213OGd6NWZzNTgifQ.BJWq3YKGRvd0iaZaofY_7Q' #jeton d'accès.


class Situation(models.Model):
    address = models.TextField()
    latitude = models.FloatField(blank = True, null=True) # blank = true sert a ce que l'utilisateur n'ai qu'a entrer l'adresse, l le modele s'occupera de la conversion des coordonnées pour lui. Et le null= true de sorte a ce que l'utilisateur  creer initialement un nvx modele, db stocke comme valeure
    longitude = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=token)
        g = g.latlng # [latitude, longitude]
        self.latitude = g[0]
        self.longitude = g[1]
        return super(Situation, self).save(*args, **kwargs)


