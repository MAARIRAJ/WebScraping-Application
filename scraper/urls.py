#scraper/urls.py  
from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstscreen, name='firstscreen'),
    path('index/', views.index, name='index'),
    path('scrape/', views.scrape, name='scrape'),
    path('processing/<str:link>/', views.processing, name='processing'),
    path('generate_download_link/<path:link>/', views.generate_download_link, name='generate_download_link'),
    path('download_excel/', views.download_excel, name='download_excel'),
]

















