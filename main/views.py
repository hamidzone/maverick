from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152355',
        'name': 'Muhammad Hamid',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)