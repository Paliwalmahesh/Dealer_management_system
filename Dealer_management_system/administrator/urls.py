from django.urls import path
from . import views
urlpatterns = [
   
     
     path('administrator_Signin',views.administrator_Signin, name='administrator_Signin'),
     path('administrator_Signup',views.administrator_Signup, name='administrator_Signup'),
    
]