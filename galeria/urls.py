from django.urls import path
from galeria.views import galeria, imagem

urlpatterns = [
    path('', galeria), 
    path('imagem/', imagem), 
]