from django.urls import path
from .views import inicio 
from produtos import views


urlpatterns = [
    path('', inicio, name="inicio"),
    path('usuarios/', views.usuarios, name="listagem_usuarios")
]