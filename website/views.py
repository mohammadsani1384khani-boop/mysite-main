from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home_page(request):
    return render(request, 'index.html')

def about_page(request):
    features = [
        {'img': 'o1.jpg', 'title': 'Rent a Car', 'desc': 'The preservation of human life is the ultimate value.'},
        {'img': 'o2.jpg', 'title': 'Cruise Booking', 'desc': 'I was always somebody who felt quite sorry for myself.'},
        {'img': 'o3.jpg', 'title': 'To Do List', 'desc': 'The following article covers a topic that has recently moved to center stage.'},
        {'img': 'o4.jpg', 'title': 'Food Features', 'desc': 'There are many kinds of narratives and organizing principles.'},
    ]
    return render(request, 'about', {'features': features})





def countent_page(request):
    return render(request, 'countent.html')


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
