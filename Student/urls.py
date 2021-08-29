from django.urls import  path
from . import views

urlpatterns = [
    path("student_home/",views.student_home,name="Student Home"),
    path("about/",views.about,name="About"),
    path("alumni_s/",views.alumni1,name="Alumni1"),
    path("events/",views.events,name="Events"),
    path("chat_box/",views.chat_box,name="ChatBox"),
    path("contact/",views.contact,name="Contact"),
    path("profile_show/",views.profile_show,name="Profile"),
    path("profile_form/",views.profile_form,name="Profile Form"),

]