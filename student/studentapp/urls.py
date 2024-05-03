from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('read',views.read,name='read'),
    path('insert',views.insert,name='insert'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('Delete/<int:id>',views.Delete,name='Delete'),

]