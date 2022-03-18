from django.http import HttpResponse
import datetime
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import New_event


class NewTaskForm(forms.Form):
    task = forms.CharField(label = "Название")
    dt_field = forms.DateTimeField(label = "Дата")

# Create your views here.
def index(request):
    #return HttpResponse("Добро пожаловать в календарь событий")
    return render(request, "diary/index.html")

#tasks = []
#datas = []
#datas.append(tasks)
def all(request):
    #news = New_event.objects.all()
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "all/index.html", {
        "new_events": New_event.objects.all(),
        "tasks": request.session["tasks"]
        #"datas": datas
    })

def viki(request):
    return HttpResponse("Добро пожаловать, Виктория, в календарь событий")

#def whoyou(request, name):
    #return HttpResponse(f"Добро пожаловать, {name.capitalize()}, в календарь событий")
    #return  render(request, "diary/whoyou.html", {
    #    "name": name.capitalize()
  #  })

def day(request):
    now = datetime.datetime.now()
    return render(request, "newday/index.html",{
        "newday": now.month == 1 and now.day == 1
    })

def event(request, id):
    event = New_event.objects.get(pk = id)
    return render(request, "event/index.html", {
        "event": event
    })

def new_event(request):
    if request.method =="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
           # dt_field = form.cleaned_data["dt_field"]
           # datas.append(dt_field)
            return HttpResponseRedirect(reverse("all"))
        else:
            return render(request, "new_event/index.html", {
                "form": form
            })

    return render(request, "new_event/index.html", {
        "form": NewTaskForm()

    })

