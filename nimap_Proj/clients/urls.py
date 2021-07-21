from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('showClients/',views.clients_list,name = 'client_list'),
    path('showProjects/',views.project_list,name = 'project_list'),
    path('create_clients/',views.CreateClients,name = 'create_clients'),
    path('create_projects/',views.CreateProjects,name = 'create_projects'),
    path('update_projects/<str:pk>/',views.updateProjects,name = 'update_projects'),
    path('delete_projects/<str:pk>/',views.deleteProject,name = 'delete_projects'),
    path('update_clients/<str:pk>/',views.updateClient,name = 'update_clients'),
    path('delete_clients/<str:pk>/',views.deleteProject,name = 'delete_client'),
    path('myview',views.myview,name = 'myview')
]