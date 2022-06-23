from django.shortcuts import render,redirect
from firstapp.models import FirstModel
from .form import PersonForms
# Create your views here.

def insertPerson(request):
    person=FirstModel.objects.all()
    return render(request, "home.html",{'people':person})


def createPerson(request):
    if request.method=='POST':
        form=PersonForms(request.POST)
        if form.is_valid():
            try:

                form.save()
                return redirect('/display')
            except:
                pass
    else :
        form=PersonForms()

    return render(request,"createperson.html",{'create':form})

def listallPeople(request):
     person=FirstModel.objects.all()
     context={
        'trainee': person
    }
     return render(request, "displaypeople.html",{ 'person': person })    
