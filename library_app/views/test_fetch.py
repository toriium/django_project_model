from django.shortcuts import render


def test_fetch(request):
    return render(request, "library_app/test_fetch.html")
