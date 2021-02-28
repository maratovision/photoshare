from django.urls import path
from .views import *


urlpatterns = [
    path('', gallery, name='gallery'),
    path('photo/<str:pk>', view_photo, name='photo'),
    path('add/', add_photo, name='add'),
]