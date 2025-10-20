from django.urls import path
from website.views import *
# http_test,json_test

urlpatterns = [
    path('',home_page),
    path('about',about_page),
    path('countent',countent_page)


    # path('http_test',http_test),
    # path('json_test',json_test)
]