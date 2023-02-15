from django.urls import path
from app1 import views

app_name="app1"

urlpatterns=[
    path('reg',views.register,name='register'),
    path('user_login',views.user_login,name='login'),
    
    
]