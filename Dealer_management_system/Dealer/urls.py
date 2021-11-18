from django.urls import path
from . import views
urlpatterns = [
     path('Dealer_order',views.Dealer_order, name='Dealer_order'),
     path('Dealer_Signup',views.Dealer_Signup, name='Dealer_Signup'),
     path('Dealer_Signin',views.Dealer_Signin, name='Dealer_Signin'),
     
     path('Dealer_delete_product/<str:pk>/', views.Dealer_delete_product, name="Dealer_delete_product"),
     path('Dealer_update_product/<str:pk>/', views.Dealer_update_product, name="Dealer_update_product"),
     path('Dealer_add_product/<str:pk>/', views.Dealer_add_product, name="Dealer_add_product"),
     path('Dealer_home',views.Dealer_home, name='Dealer_home'),
    
]