from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homes.as_view(),name='home'),
    path('post/<int:pk>/',views.detailview.as_view(),name='detailview'),
    #path('p/',views.hello,name='hello')
    path('new_post/',views.createview.as_view(),name='createpost'),
    path('new_post/<int:pk>',views.editPost.as_view(),name='editPost'),
    path('delete_post/<int:pk>',views.deletepost.as_view(),name='deletePost')
]

