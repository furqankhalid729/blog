from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import post
# Create your views here.

class homes(ListView):
    model=post
    template_name ='home.html'


class detailview(DetailView):
    model = post
    template_name = 'detailview.html'


class createview(CreateView):
    model=post
    template_name='new_post.html'
    fields=['Title','Author','Body']

class editPost(UpdateView):
    model = post
    template_name = 'editPost.html'
    fields = ['Title', 'Body']

class deletepost(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
