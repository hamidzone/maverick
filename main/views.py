from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Display the main page with mood entries
def show_main(request):
    mood_entries = Product.objects.all()
    context = {
        'npm': '2306152355',
        'name': 'Muhammad Hamid',
        'class': 'PBP E',
        'mood_entries': mood_entries,
    }
    return render(request, "main.html", context)

# Handle creating new mood entries
def create_mood_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST" :
        form.save()
        return redirect('main:show_main')

    context = {'form': form}

    return render(request, "create_mood_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")