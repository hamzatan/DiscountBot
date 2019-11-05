from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request,'tracker/index.html')
