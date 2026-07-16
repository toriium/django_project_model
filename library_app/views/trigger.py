from django.http import Http404


def trigger_404(request):
    raise Http404("This page does not exist.")


def trigger_500(request):
    raise Exception("Intentional server error for testing.")
