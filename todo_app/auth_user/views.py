from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from todo_app.auth_user.models import Profile
from todo_app.tasks.models import Task
from todo_app.auth_user.forms import ProfileCreateForm, ProfileLoginForm, EditProfileForm, DeleteProfileForm

from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import logout
from django.views import generic as views

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match")

        return cleaned_data


class LoginUserView(auth_views.LoginView):
    form_class = ProfileLoginForm
    template_name = '../templates/auth_user/profile-login.html'
    redirect_authenticated_user = True


class LogoutUserView(auth_views.LogoutView):
    pass


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileDetailsView(views.TemplateView):
    template_name = '../templates/auth_user/profile-details.html'

    def get_context_data(self, **kwargs):
        profile = self.request.user
        all_tasks = Task.objects.filter(user=self.request.user)
        full_name = f'{profile.first_name} {profile.last_name}'

        context = {
            'profile': profile,
            'all_tasks': all_tasks,
            'full_name': full_name,
        }
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = '../templates/auth_user/profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteProfileView(views.FormView):
    form_class = DeleteProfileForm
    template_name = '../templates/auth_user/profile-delete.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        profile = self.request.user
        profile.delete()
        logout(self.request)
        return super().form_valid(form)