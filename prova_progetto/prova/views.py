from django.http import HttpResponse

def home_page(request):
    response = "Benvenuto nella Homepage!\n"
    return HttpResponse(response)

def ausGP_page(request):
    response = "Charles Leclerc wins the Australian GP!"
    return HttpResponse(response)