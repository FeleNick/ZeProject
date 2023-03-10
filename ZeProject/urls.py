"""ZeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views as myapp_views
from register import views as v
from CNjokes import views as j

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('register/', v.RegisterView.as_view(), name="register"),
    path('', include("django.contrib.auth.urls")),
    path('jokes/', j.LikedJokesView.as_view(), name="jokes"),
    path('joke/', j.CNJokeView.as_view(), name="joke"),
    path('most-liked-jokes/', j.MostLikedJokesView.as_view(), name='most_liked_jokes'),
    path('jokes/<int:pk>/delete/', j.CannotDeleteView.as_view(), name='delete_joke'),

]
