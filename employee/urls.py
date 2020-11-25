from django.urls import path
from .import views as v

urlpatterns = [
    path("", v.home, name="home"),
    path("add", v.add, name="addemp"),
    path('vemployee', v.vemp, name='viewemployeepage'),
]