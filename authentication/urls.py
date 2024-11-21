from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('tasks/create/', views.create_task_view, name='create_task'),
    path('tasks/assigned/', views.view_task_assigned_view, name='view_task_assigned'),
    path('tasks/created/', views.view_task_created_view, name='view_task_created'),
    path('tasks/update/<str:taskUid>/', views.update_task_view, name='update_task'),
    path('tasks/delete/<str:taskUid>/', views.delete_task_view, name='delete_task'),
]