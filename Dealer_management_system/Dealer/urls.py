from django.urls import path
from . import views
urlpatterns = [
     path('Dealer_Signin',views.Dealer_Signin, name='Dealer_Signin'),
     path('Dealer_Signup',views.Dealer_Signup, name='Dealer_Signup'),
    
]