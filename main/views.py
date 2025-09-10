from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406496253',
        'name': 'Tazkia Nur Alyani',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)

# Create your views here.
