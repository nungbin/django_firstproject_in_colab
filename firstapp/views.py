from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Booking

# Create your views here.
def index(request):
    objs=Booking.objects.all()
    context={
      "objs": objs
    }
    return render(request, "index.html", context)

def hello_world(request):
    return HttpResponse("Hello World")

class helloTaiwan(View):
      def get(self, request):
          return HttpResponse("Hello Taiwan 3")