from django.http import HttpResponse

def home_page(request):
    response = "Benvenuto nella Homepage!\n"
    response += "Sono andato a capo...dieci\n"

    return HttpResponse(response)

def home(request):
    response = "Hello world! Forza Ferrari!"
    return HttpResponse(response)