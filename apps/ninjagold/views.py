from django.shortcuts import render, redirect
from time import strftime, gmtime
from random import randint
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "index.html")

def processmoney(request):
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if request.POST['building'] == "reset":
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['gained'] = True
    if request.POST['building'] == "farm":
        i = randint(10, 20)
        request.session['activities'].insert(0,"<p style='color: green;'>Earned "+str(i)+" gold(s) from the farm! ("+time+")</p>")
        request.session['gold'] += i
        request.session['gained'] = True
    if request.POST['building'] == "cave":
        i = randint(5, 10)
        request.session['activities'].insert(0,"<p style='color: green;'>Earned "+str(i)+" gold(s) from the cave! ("+time+")</p>")
        request.session['gold'] += i
        request.session['gained'] = True
    if request.POST['building'] == "house":
        i = randint(2, 5)
        request.session['activities'].insert(0,"<p style='color: green;'>Earned "+str(i)+" gold(s) from the house! ("+time+")</p>")
        request.session['gold'] += i
        request.session['gained'] = True
    if request.POST['building'] == "casino":
        i = randint(-50, 50)
        if i >= 0:
            request.session['activities'].insert(0,"<p style='color: green;'>Earned "+str(i)+" gold(s) from the casino! ("+time+")</p>")
            request.session['gained'] = True
        else:
            request.session['activities'].insert(0,"<p style='color: red;'>Lost "+str(abs(i))+" gold(s) from the casino! ("+time+")</p>")
            request.session['gained'] = False
        request.session['gold'] += i
    return redirect("/")
