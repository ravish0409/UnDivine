from django.urls import path
from rate import views

urlpatterns = [
    path('upload/', views.upload_meme, name='upload_photos'),
    path('', views.home, name='home'),
]
