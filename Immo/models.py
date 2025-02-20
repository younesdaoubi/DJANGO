from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from map.models import Situation


class Post(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal(1))])
    surface = models.DecimalField(default=0, max_digits=9, decimal_places=0, validators=[MinValueValidator(Decimal(1))])
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    situation = models.ForeignKey(Situation, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
