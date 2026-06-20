from django.urls import path
from . import views

urlpatterns =[
    path('',views.signup, name = 'home'),
    path('login/', views.login, name = 'login'),
    path('todo_list/',views.todo_list, name='todo_list'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:todo_id>/',views.delete_todo, name='delete_todo'),
    path('signout/', views.signout, name='signout'),
]
         
