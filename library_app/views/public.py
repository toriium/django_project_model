
from django.contrib.auth.decorators import login_not_required
from django.shortcuts import render



@login_not_required
def public(request):
    return render(request, "library_app/public.html")
