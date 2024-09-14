from django.urls import path
from galeria.views import galeria, imagem, buscar

urlpatterns = [
    path('', galeria, name='index'), 
    path('imagem/<int:foto_id>', imagem, name='imagem'), 
    path('buscar', buscar, name="buscar")
]