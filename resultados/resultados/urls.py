# resultados/urls.py (archivo principal de URL)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notas.urls')),  # Incluir las URLs de la aplicación notas
]
