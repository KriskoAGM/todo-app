from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from todo_app.auth_user.models import Profile


class ProfileCreateForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Password'}),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Confirm Password'}),
        strip=False,
    )
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

class ProfileLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True})
    )
