
from django import forms
from map.forms import SituationtForm
from map.models import Situation
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'price', 'surface', 'content', 'date_posted', 'author', 'image', 'situation']