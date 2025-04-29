from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('adminpanel', views.admin_dashboard, name='admin_dashboard'),
    path('admin/news/edit/<int:id>/', views.edit_news, name='edit_news'),
    path('admin/news/delete/<int:id>/', views.delete_news, name='delete_news'),
    path('admin/view-all-news/', views.view_all_news, name='view_all_news'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/news/add/latest/', views.add_latest_news, name='add_latest_news'),
    path('admin/news/add/headline/', views.add_headline_news, name='add_headline_news'),
    path('news/edit/<int:id>/', views.edit_news, name='edit_news'),
    path('admin/manage-ads/', views.manage_ads, name='manage_ads'),
    path('news/latest/', views.view_all_latest_news, name='view_all_latest_news'),
    path('headline/', views.view_all_headline_news, name='view_all_headline_news'),


    

    # Add other paths for individual news details or other views as needed
]
