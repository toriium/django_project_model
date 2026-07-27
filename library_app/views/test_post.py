from django.shortcuts import render


def test_post(request):
    return render(request, "library_app/test_post.html")
