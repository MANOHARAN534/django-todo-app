# myproject/urls.py
from django.contrib import admin
from django.urls import path
from todo import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), # Main page-ku index view
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'), 
]
