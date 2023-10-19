from django.shortcuts import render,redirect

# Create your views here.
def home (request):
    return render(request,"home.html")

from . form import *
def first(request):
    if request.method=="POST":
        obj=ClientForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={
            "form":ClientForm
        }
        return render(request,"first.html",d)


from . models import *
def clientdetails(request):
    data=Client.objects.all()
    print(data)
    d={
        "data":data
    }
    return render (request,"clientdetails.html",d)

def addProject(request):
    if request.method=="POST":
        obj=ProjectForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={
            "form":ProjectForm
        }
        return render(request,"first.html",d)


def projectdetails(request):
    data=Project.objects.all()
    d={
        "data":data
    }
    return render (request,"projectdetails.html",d)

def del1(request):
    uid=request.GET.get("id")
    obj=Client.objects.get(id=uid)
    obj.delete()
    return redirect("/clientdetails")

def del2(request,uid):
    obj=Client.objects.get(id=uid)
    obj.delete()
    return redirect("/clientdetails")

def edit(request,uid):
    obj=Client.objects.get(id=uid)
    if request.method=="POST":
        obj=ClientForm(request.POST,instance=obj)
        obj.save()
        return redirect("/clientdetails")
    else:
        d={
            "form":ClientForm(instance=obj)
        }
        return render(request,"first.html",d)
