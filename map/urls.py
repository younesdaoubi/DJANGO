from django.urls import path
from .views import SituationView


urlpatterns = [
    path('post/<int:pk>', SituationView.as_view(), name ='post-detail')
]

