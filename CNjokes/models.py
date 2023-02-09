from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class CNJoke(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joke = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.joke