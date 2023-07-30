from django.urls import path

from todo_app.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='home'),
]