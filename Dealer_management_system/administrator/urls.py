from django.urls import path
from . import views
urlpatterns = [
   
     path('administrator_Get_details/<str:pk>/', views.administrator_Get_details, name="administrator_Get_details"),
     path('administrator_Signin',views.administrator_Signin, name='administrator_Signin'),
     path('administrator_Signup',views.administrator_Signup, name='administrator_Signup'),
     path('administrator_home',views.administrator_home, name='administrator_home'),
     path('adminstrator_add_Product',views.adminstrator_add_Product,name='adminstrator_add_Product'),
     path('administrator_products_view',views.administrator_products_view,name='administrator_products_view'),
     path('administrator_Pending_order_view',views.administrator_Pending_order_view, name='administrator_Pending_order_view'),
     path('administrator_Send_back_order_view',views.administrator_Send_back_order_view, name='administrator_Send_back_order_view'),
     path('administrator_delivered_order_view',views.administrator_delivered_order_view, name='administrator_delivered_order_view'),
     path('administrator_Approved_order_view',views.administrator_Approved_order_view, name='administrator_Approved_order_view'),
    
]