from django.urls import path
from website.views import *

urlpatterns = [
    path('', home_page),                    # صفحه اصلی بدون name
    path('about/', about_page, name='about'),   # اضافه کردن name
    path('countent/', countent_page),
]
