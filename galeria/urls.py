from django.urls import path
from galeria.views import galeria, imagem

urlpatterns = [
    path('', galeria, name='index'), 
    path('imagem/', imagem, name='imagem'), 
]