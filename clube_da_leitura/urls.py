from django.contrib import admin
from django.urls import path
from colecao.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('home/', home),
    path('home/', home),
    path('home/', home),
    path('home/', home),
]
