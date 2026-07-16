from django.shortcuts import render


def home(request):
    return render(request, "library_app/home.html")
