from datetime import date
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from Student.models import Profile
from .decorator import *
from .models import *
from .forms import *
from .Sending_messages import *
# Create your views here.


    
@allowed_users(allowed_roles=['admin','staff'])
def about(request):
    return render(request,"about.html")


def alumni(request):
      alumni=Profile.objects.all()
      return render(request,"alumni.html",{"alumni":alumni})
      
@allowed_users(allowed_roles=['admin','staff'])
def home(response):
    return render(response,"home.html")


def logout_request(request):
    logout(request)
    return render(request,"home.html")



@allowed_users(allowed_roles=['admin','staff'])
def create_announcement(response):
    if response.method == "POST":
        form=createnewannouncement(response.POST)

        if form.is_valid():
            t=form.cleaned_data["text"]
            a=Announcements(text=t)
            a.save()
            
            if form.cleaned_data["check"]==True:
                send_message(t)
                messages.success(response,'Announcement was saved and messages are sent')
            else:
                messages.success(response,'Announcement was saved')
            return render(response,"home.html",{})
    else:
        form=createnewannouncement()
        return render(response,"announcement.html",{"form":form})


@allowed_users(allowed_roles=['admin','staff'])
def create_event(response):
    if response.method == "POST":
        form=schedule_event(response.POST)

        if form.is_valid():
            c1=form.cleaned_data["subject"]
            c2=form.cleaned_data["date"]
            c3=form.cleaned_data["time_start"]
            c4=form.cleaned_data["time_end"]
            c=Event(subject=c1,date=c2,time_start=c3,time_end=c4)
            c.save()
            t="You have a {0} extra Event on {1} from {2} to {3}".format(str(c1),str(c2),str(c3),str(c4))
            if form.cleaned_data["check"]==True:
                send_message(t)
                messages.success(response,'Event is scheduled and messages are sent')
            else:
                 messages.success(response,'Event is scheduled')
            return render(response,"home.html",{"text":t})
    else:
        form=schedule_event()
        return render(response,"Event.html",{"form":form})

 
#alert
