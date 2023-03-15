from django.contrib import admin
from django.urls import path
from lin_lout import views
import  lin_lout.views as views
app_name = 'lin_lout'


urlpatterns = [
  
    path('', views.HOME, name='home'),
    # path('login/', views.LOGIN_VIEW, name='login'),
    # path('register/', views.REGISTRATION, name='register'),
    # path('logout/', views.LOGOUT, name='logout'),
    # path('verify_otp/', views.VERIFY_OTP, name='verify_otp'),
    # path('end_register/', views.END_REGISTER, name='end_register'),
    # path('forgot_password/', views.FORGOT_PSW, name='for_pswd'),
    # path('ver_otp/', views.VERIFY_RESET_OTP, name='Verify_OTP'),
    # path('reset_password/', views.RESET_PASSWORD, name='reset_psw'),
]

