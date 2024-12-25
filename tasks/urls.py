from xml.etree.ElementInclude import include

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_task, name='create_task'),
    path('task/<int:pk>', views.detail_task, name='detail_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('update/<int:pk>', views.update_task, name='update_task'),
]
