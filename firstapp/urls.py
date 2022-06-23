from .import views
from django.urls import path

urlpatterns=[
    #path("create", views.insertPerson,name="create"),
    path("create", views.createPerson,name="create"),
    path("display", views.listallPeople,name="display")
]