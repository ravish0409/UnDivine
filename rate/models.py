from django.db import models

class Meme(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image1 = models.ImageField(upload_to='memes')
    image2 = models.ImageField(upload_to='memes')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
