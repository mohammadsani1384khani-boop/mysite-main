from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def home_page(request):
    return render(request,'index.html')

def about_page(request):
    features = range(1, 5)  # اعداد 1 تا 4
    return render(request, 'about.html', {'features': features})


def countent_page(request):
    return render(request,'countent.html')


# def home_page(request):
#     return HttpResponse("home_page")

# def about_page(request):
#     return HttpResponse("about_page")

# def countent_page(request):
#     return HttpResponse("countent_page")


# def http_test(request):
#     return HttpResponse("hi maryam ")

# def json_test(request):
#     return JsonResponse({'name':"ali"})

# Create your views here.
