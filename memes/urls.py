

from django.urls import path
from memes import views
urlpatterns = [
    path('', views.meme_list, name='meme_list'),
    path('upload/', views.upload_meme, name='upload_meme'),
]
