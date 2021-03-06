"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from enroll.views import add_show , delete_data , update_data , sign_up , login , user_profile , user_logout , change_pass , home

urlpatterns = [
    path('Signup', sign_up, name="Signup"),
    path('login/', login, name="Login"),
    path('profile/', user_profile, name="profile"),
    path('logout/', user_logout, name="logout"),
    path('changepass/', change_pass, name="Changepass"),
    path('crud/<int:id>', add_show, name="AddShow"),
    path('', home, name="Home"),
    path('admin/', admin.site.urls),
    path('delete/<int:id>/', delete_data,name="Delete_Data"),
    path('update/<int:id>/', update_data,name="Update_Data"),
]
