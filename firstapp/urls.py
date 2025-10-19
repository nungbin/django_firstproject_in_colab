from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('function', views.hello_world),
  path('class', views.helloTaiwan.as_view()),
]