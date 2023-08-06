from django.urls import path

from todo_app.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home_page, name='home'),
]