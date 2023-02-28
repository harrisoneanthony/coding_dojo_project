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
    # path('target_search', views.target_search),
    path('view_event/<int:id>', views.view_event),
    path('unjoin/<int:id>',views.unjoin_event),
    path('join/<int:id>',views.join_event),
    path('account/<int:id>', views.view_account),
    path('update_user/<int:id>', views.update_user),
    path('create_message/<int:id>',views.create_message),
    path('delete_message/<int:id>/<int:ide>',views.delete_message),
    path('edit_message/<int:id>/<int:ide>',views.edit_message),
    path('message_edited/<int:id>/<int:ide>',views.message_edited),
]
