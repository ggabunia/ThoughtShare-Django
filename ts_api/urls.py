from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from ts_api import views
from rest_framework import routers

app_name = 'ts_api'
urlpatterns = [
    path('', views.api_root),
    path('rest-auth/', include('rest_auth.urls'), name='rest_auth'),
    path('all-ideas/',views.AllIdeas.as_view(), name = 'all_ideas'),
    path('my-ideas/',views.UserIdeas.as_view(), name = 'user_ideas'),
    path('my-ideas/<int:pk>',views.UserIdeas.as_view(), name = 'user_ideas'),
    path('all-users/',views.UserList.as_view(), name = 'user_list'),
    path('register/',views.RegisterUser.as_view(), name = 'register'),
    path('add-idea/',views.AddIdea.as_view(), name = 'add_idea'),
    path('get-user/',views.GetUser.as_view(), name = 'get_user'),
    path('get-user/<int:pk>',views.GetUser.as_view(), name = 'get_user'),
    path('all-categories/',views.CategoryList.as_view(), name = 'all_categories'),
    path('get-category/',views.GetCategory.as_view(), name = 'get_category'),
    path('get-category/<int:pk>',views.GetCategory.as_view(), name = 'get_category'),
    path('edit-idea/',views.UpdateIdea.as_view(), name = 'edit_idea'),
    path('edit-idea/<int:pk>',views.UpdateIdea.as_view(), name = 'edit_idea'),

]
