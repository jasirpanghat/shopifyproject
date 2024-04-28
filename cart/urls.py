from django.urls import path
from .views import *


urlpatterns = [
    path('AddCart/<int:id>',AddCart.as_view(),name='add_cart'),
    path('ViewCart/',Viewcart.as_view(),name='viewcart'),
    path('update-cart/', UpdateCartView.as_view(), name='update_cart'),
    path('Deletecart/<int:cart_id>',delete_cart,name='deletecart'),
    path('Updatetotal/',cart_total_view,name='update_total'),
    
]