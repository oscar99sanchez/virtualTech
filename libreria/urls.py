from http.client import ImproperConnectionState
from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('MS', views.libros, name='MS'),
    path('DD', views.DD, name='DD'),
    path('MN', views.MN, name='MN'),
    path('MP', views.MP, name='MP'),
    path('TC', views.TC, name='TC'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('singup', views.singup, name='singup'),
    path('logout', views.singout, name='logout'),
    path('singin', views.singin, name='singin'),


    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)