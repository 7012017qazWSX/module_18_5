from django.shortcuts import render

# Create your views here.
# python manage.py runserver

def films(request):
    return render(request, 'main.html')

def cinemas(request):
    context ={
        'my_films': ['Врата Балдура 3', 'Warhammer 40000 Ересь Хоруса', 'Судья Дредд']
    }
    return render(request, 'cinema.html', context)

def tickets(request):
    return render(request, 'ticket.html')