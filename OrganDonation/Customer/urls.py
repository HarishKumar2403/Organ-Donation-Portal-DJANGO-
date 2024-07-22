
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('send_otp/Register/',views.register,name='register'),
    path('Login/',views.user_login,name='user_login'),
    path('admin/',views.user_admin,name='user_admin'),
    path('edit_users/<int:id>/',views.edit_users,name='edit_users'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('form/',views.donation_form,name='donation_form'),
    path('send_otp/',views.send_otp,name='send_otp'),
    path('404/',views.page_404,name='page_404'),
    path('hospital_login/',views.Hospital_login,name='Hospital_login'),
    path('hospital/<int:id>/',views.Hospital_main,name='Hospital_main'),
    path('hospital_logout/',views.Hospital_logout,name='Hospital_logout')
   
]
