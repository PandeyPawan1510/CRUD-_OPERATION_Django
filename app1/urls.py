from django.urls import path
from .import views
urlpatterns = [
    path("",views.home),
    path("addclient", views.first),
    path("clientdetails", views.clientdetails),
    path("addProject",views.addProject),
    path("projectdetails",views.projectdetails),
    path("del1",views.del1),
    path("del2/<int:uid>", views.del2),
    path("edit/<int:uid>",views.edit)
]
