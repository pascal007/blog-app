from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.permissions import AllowAny

from django.contrib.auth.views import LoginView

from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm
from .serializers import CreateUserSerializer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_form_class(self):
        return AuthenticationForm

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            messages.success(self.request, f"Welcome, {user.username}!")
            return HttpResponseRedirect(reverse_lazy('post_list'))
        else:
            form.add_error(None, 'Invalid username or password.')
            return self.form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('post_list'))
        return super().dispatch(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class SignupView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()
