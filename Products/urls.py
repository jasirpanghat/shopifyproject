from django.urls import path
from . import views


urlpatterns = [
    path('AddProduct/',views.add_products,name='addproducts'),
    path('AddColour/',views.add_colour,name='addcolour'),
    path('AddSize/',views.add_size,name='addsize'),
    path('ViewProducts/',views.view_product,name='viewproducts'),
    path('UnlistProduct/<int:id>',views.unlist_product,name='unlist_product'),
    path('Editproduct/<int:id>',views.edit_product,name='editproduct'),
    path('Unlistproduct/',views.view_unlist,name="unlist_products"),
    path('Listproduct/<int:id>',views.list_product,name='List_product'),
    path('get_stock_data/',views.get_stock_data,name="get_stock_data")
    
]
