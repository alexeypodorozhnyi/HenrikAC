from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from . import forms


class MyLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('blog:list'))
        return super().get(request, *args, **kwargs)


class SignUpView(generic.CreateView):
    form_class = forms.UserCreateForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('blog:list')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('blog:list'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        new_user = authenticate(self.request, username=username, password=password)
        login(self.request, new_user)
        return valid
