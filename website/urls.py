from django.urls import path
from .views import home_page, about_page, countent_page

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('countent/', countent_page, name='countent'),
]
