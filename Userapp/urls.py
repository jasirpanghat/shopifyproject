from django.urls import path
from . import views

urlpatterns = [
        path('login/',views.user_login,name='login'),
        path('',views.user_home),
        path('UserSign/',views.user_signup,name='User_sign'),
        path('UserSignUp/,',views.user_signup,name='SignUp'),
        path('otp',views.otp,name='otp'),
        
    ]