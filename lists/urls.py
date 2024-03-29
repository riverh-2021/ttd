"""suplerlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,re_path
from lists import views


urlpatterns = [
    path('new',views.new_list,name='new_list'),
    re_path(r'^(\d+)/$',views.view_list,name='view_list'),
    re_path(r'^(\d+)/add_item$',views.add_item,name='add_item'),
   # path(r'^$',views.home_page,name='home'),
    #1path('',views.home_page,name='home'),
    #path('lists/the-only-list-in-the-world/', views.view_list,name='view_list'),
    #2path('lists/new',views.new_list,name='new_list'),
    #3re_path(r'^lists/(\d+)/$',views.view_list,name='view_list'),
    #4re_path(r'^lists/(\d+)/add_item$',views.add_item,name='add_item'),
  #  re_path(r'^lists/(.+)/$',views.view_list,name='view_list'),
    ]

