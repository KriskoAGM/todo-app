from django.shortcuts import render
from django.urls import reverse_lazy

from todo_app.auth_user.models import Profile
from todo_app.auth_user.forms import ProfileCreateForm, ProfileLoginForm

from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from django.views import generic as views

from django.contrib.auth.decorators import login_required


# Create your views here.


class RegisterUserView(views.CreateView):
    model = Profile
    template_name = '../templates/auth_user/profile-register.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        return response


class LoginUserView(auth_views.LoginView):
    form_class = ProfileLoginForm
    template_name = '../templates/auth_user/profile-login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')


class LogoutUserView(auth_views.LogoutView):
    pass


@login_required(login_url='login')
def profile_details(request):
    profile = request.user

    context = {
        'profile': profile,
    }

    return render(request, '../templates/auth_user/profile-details.html', context=context)