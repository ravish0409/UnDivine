from django.db import models

class Meme(models.Model):
    image = models.ImageField(upload_to='memes/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
