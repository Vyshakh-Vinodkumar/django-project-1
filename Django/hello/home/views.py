from django.shortcuts import render,HttpResponse
from home.models import Feedback
# from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is Home Page")
def about(request):
    return render(request,"feedback.html")
def contact(request):
    return render(request,"contacts.html")
def pythond(request):
    return render(request,"pythond.html")
def pythonmt(request):
    return render(request,"pythonmt.html")
def pythonat(request):
    return render(request,"pythonat.html")
def apti(request):
    return render(request,"apti.html")
def verbal(request):
    return render(request,"verbal.html")
def feedback(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        desc=request.POST.get('desc')
        feedback=Feedback(name=name,phoneno=phoneno,email=email,desc=desc)
        feedback.save()
    return render(request,"feedback.html")