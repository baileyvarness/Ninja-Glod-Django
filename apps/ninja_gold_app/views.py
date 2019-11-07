from django.shortcuts import render, HttpResponse, redirect
from random import randint

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = ""
    return render(request, "index.html")

def process_money(request):
    print("Find Gold Was Clicked")
    if request.POST['location'] == 'farm':
        number = randint(10,20)
        request.session['counter'] += number
        request.session['farm'] = True
        request.session['activities'] = (f"Earned {number} golds from the farm")
        print(number)
    if request.POST['location'] == 'cave':
        number = randint(5,10)
        request.session['counter'] += number
        request.session['cave'] = True
        request.session['activities'] = (f"Earned {number} golds from the cave")
        print(number)
    if request.POST['location'] == 'house':
        number = randint(2,5)
        request.session['counter'] += number
        request.session['house'] = True
        request.session['activities'] = (f"Earned {number} golds from the house")
        print(number)
    if request.POST['location'] == 'casino':
        number = randint(-50,50)
        request.session['counter'] += number
        print(number)
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")