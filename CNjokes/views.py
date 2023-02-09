from django.shortcuts import render, redirect
from .forms import CNJokeForm
from .models import CNJoke
import requests

# Create your views here.
def cnjoke_view(request):
    if request.method == 'POST':
        form = CNJokeForm(request.POST)
        if form.is_valid():
            cnjoke = form.save(commit=False)
            cnjoke.user = request.user
            cnjoke.save()
            return redirect('jokes')
    else:
        joke = requests.get('https://api.chucknorris.io/jokes/random').json()['value']
        form = CNJokeForm(initial={'joke': joke})
    return render(request, 'cnjokes/cnjoke.html', {'form': form})

def likedjokes_view(request):
    liked_jokes = CNJoke.objects.filter(user=request.user)
    return render(request, 'cnjokes/likedjokes.html', {'liked_jokes': liked_jokes})
