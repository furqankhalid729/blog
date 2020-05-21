from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView
from .models import post
# Create your views here.

class homes(ListView):
    model=post
    template_name ='home.html'


class detailview(DetailView):
    model = post
    template_name = 'detailview.html'



def hello(a):
   return HttpResponse("hello")