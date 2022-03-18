from django.urls import path

from . import views

#app_name = "all"
urlpatterns = [
    path("", views.index, name = "index"),
    path("viki", views.viki, name = "viki"),
    #path("<str:name>", views.whoyou, name = "whoyou"),
    path("day", views.day, name = "day"),
    path("new_event", views.new_event, name = "new_event"),
    path("all", views.all, name = "all"),
    path("<int:id>", views.event, name="event")
]