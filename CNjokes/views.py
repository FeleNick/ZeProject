from django.shortcuts import render, redirect
from django.db.models import Count
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .forms import CNJokeForm
from .models import CNJoke
import requests

class CNJokeView(LoginRequiredMixin, CreateView):
    template_name = 'cnjokes/cnjoke.html'
    form_class = CNJokeForm
    success_url = reverse_lazy('jokes')
    model = CNJoke

    def get_initial(self):
        joke = requests.get('https://api.chucknorris.io/jokes/random').json()['value']
        return {'joke': joke}

    def form_valid(self, form):
        joke = form.save(commit=False)
        joke.user = self.request.user
        joke.save()
        joke.liked_by.add(self.request.user)
        return super().form_valid(form)

class LikedJokesView(LoginRequiredMixin, ListView):
    template_name = 'cnjokes/likedjokes.html'
    model = CNJoke

    def get_queryset(self):
        return CNJoke.objects.filter(user=self.request.user)
    

class MostLikedJokesView(ListView):
    template_name = 'cnjokes/most_liked_jokes.html'
    model = CNJoke

    def get_queryset(self):
        return CNJoke.objects.annotate(likes=Count('liked_by')).order_by('-likes')[:5]
        
