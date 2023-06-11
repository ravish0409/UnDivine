from django.shortcuts import render, redirect
from .forms import MemeForm
from .models import Meme

def upload_meme(request):
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemeForm()
    return render(request, 'upload_photos.html', {'form': form})

def home(request):
    memes = Meme.objects.all()
    return render(request, 'home.html', {'memes': memes})
