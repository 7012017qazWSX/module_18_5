from django.shortcuts import render

# Create your views here.

def films(request):
    return render(request, 'main.html')

def cinemas(request):
    return render(request, 'cinema.html')

def tickets(request):
    return render(request, 'ticket.html')
