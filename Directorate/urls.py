from django.urls import  path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    
    path("announcement/",views.create_announcement,name="Announcement"),
    path("event/",views.create_event,name="Event"),
    path("about/",views.about,name="About"),
    path("alumni/",views.alumni,name="Alumni"),
   
    path("logout/",views.logout_request,name="logout"),
   

    
]