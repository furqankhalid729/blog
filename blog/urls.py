from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homes.as_view(),name='home'),
    path('post/<int:pk>/',views.detailview.as_view(),name='detailview'),
    #path('p/',views.hello,name='hello')
]

