from django.shortcuts import render
from django.http import HttpResponse
import random

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrtsuvwxyz')
    generated_password = ''

    lenght = int(request.GET.get('lenght'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('*-}{?¡#$"%&/('))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for x in range(lenght):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {
        'password': generated_password
    })