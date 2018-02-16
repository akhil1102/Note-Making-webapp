from django.urls import path
from django.conf.urls import url

from notes import views


urlpatterns = [
    path('all/', views.list, name='index'),
    path('create/', views.create, name='create'),       #or ('url', <appname>.views.<function_name>
    path('edit/<id>/', views.note_edit, name='note_edit'),
    path('detail/<id>/', views.note_detail, name='note_detail'),
    path('delete/<id>', views.note_delete,name='note_delete'),
]