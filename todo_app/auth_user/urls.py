from django.urls import path

from todo_app.auth_user import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('edit/', views.EditProfileView.as_view(), name='edit-profile'),
    path('delete/', views.DeleteProfileView.as_view(), name='delete-profile'),
]