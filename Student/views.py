from Student.models import *
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from Directorate import models as mo
from College import models as us

from . forms import *

# Create your views here.
def student_home(request):
      return render(request,"student_home.html")

def about1(request):
      return render(request,"about1.html")

def alumni1(request):
      alumni1=Profile.objects.all()
      return render(request,"alumni1.html",{"alumni":alumni1})

def events(request):
      events=mo.Event.objects.all()
      announcements=mo.Announcements.objects.all()
      return render(request,"events.html",{"events":events,"announcements":announcements})

def contact(request):
      return render(request,"contact.html")

def profile_show(request):
      
      return render(request,"profile_show.html",{})

def profile_form(request):
      return render(request,"profile_show.html")

def chat_box(request):
      chatbox=ChatBox.objects.all()
      form=sendmessage(request.POST)
      if request.method == "POST":
            
            if form.is_valid():
                  n=form.cleaned_data["name"]
                  b=form.cleaned_data["body"]

                  a=ChatBox(name=n,body=b)
                  a.save()
            
                  return render(request,"chat_box.html",{"form":form,"chatbox":chatbox})
            else:
                  return render(request,"chat_box.html",{"form":form,"chatbox":chatbox})
      else:
            return render(request,"chat_box.html",{"form":form,"chatbox":chatbox})

    
      
      
