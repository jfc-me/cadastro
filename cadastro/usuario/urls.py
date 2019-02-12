
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name="login"),
    path('logout/', views.sair, name="logout"),
    path('', views.index, name="index"),
]
