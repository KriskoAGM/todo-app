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
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Profile.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters.")
        return password1


class ProfileLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True})
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'first_name', 'last_name', 'profile_picture']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age is not None and age < 0:
            raise forms.ValidationError("Age must be a positive integer.")
        return age

class DeleteProfileForm(forms.Form):
    pass