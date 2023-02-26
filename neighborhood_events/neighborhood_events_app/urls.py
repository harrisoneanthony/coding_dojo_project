from django.urls import path     
from . import views

urlpatterns = [
    path('', views.register),
    path('login/', views.login),
    path('login_user',views.login_user),
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('create_user', views.create_user),
    path('logout', views.logout),   
    path('create/event', views.create_event_page),
    path('create_event', views.create_event),
    path('search', views.search),
    path('view_event/<int:id>', views.view_event),
    path('join/<int:id>',views.join_event),
    path('unjoin/<int:id>',views.unjoin_event),
]
