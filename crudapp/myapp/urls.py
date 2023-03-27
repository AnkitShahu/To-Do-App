from django.urls import path
from .views import task_list, task_create, task_update, task_delete, loginu, user_logout, sign_up

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:pk>/', task_update, name='task_update'),
    path('delete/<int:pk>/', task_delete, name = 'task_delete'),
    path('login/', loginu, name = 'loginu'),
    path('logout/', user_logout, name = 'loginout'),
    path('signup/', sign_up, name='sign_up')
]
