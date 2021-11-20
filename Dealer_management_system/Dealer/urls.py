from django.urls import path
from . import views
urlpatterns = [
     path('Dealer_order',views.Dealer_order, name='Dealer_order'),
     path('Dealer_Signup',views.Dealer_Signup, name='Dealer_Signup'),
     path('Dealer_Signin',views.Dealer_Signin, name='Dealer_Signin'),
     path('Dealer_delete_product/<str:pk>/', views.Dealer_delete_product, name="Dealer_delete_product"),
     path('Dealer_update_product/<str:pk>/', views.Dealer_update_product, name="Dealer_update_product"),
     path('Dealer_add_product/<str:pk>/', views.Dealer_add_product, name="Dealer_add_product"),
     path('Dealer_delete_order/<str:pk>/', views.Dealer_delete_order, name="Dealer_delete_order"),
     path('Dealer_order_details_view/<str:pk>/', views.Dealer_order_details_view, name="Dealer_order_details_view"),
     path('Dealer_home',views.Dealer_home, name='Dealer_home'),
     path('Dealer_Pending_order_view',views.Dealer_Pending_order_view, name='Dealer_Pending_order_view'),
     path('Dealer_Send_back_order_view',views.Dealer_Send_back_order_view, name='Dealer_Send_back_order_view'),
     path('Dealer_delivered_order_view',views.Dealer_delivered_order_view, name='Dealer_delivered_order_view'),
     path('Dealer_Approved_order_view',views.Dealer_Approved_order_view, name='Dealer_Approved_order_view'),
]