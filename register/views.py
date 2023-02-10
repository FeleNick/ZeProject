from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm

class RegisterView(CreateView):
    template_name = "register/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response