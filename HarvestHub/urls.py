from django.urls import path
from . import views
 
urlpatterns= [
    path('', views.graph_view, name="Graph"),
    
    path('weather_report', views.weather_report, name="weather_report"),
    path('register', views.register_farmer, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('manager_dashboard', views.farmer_manager_dashboard, name='manager_dashboard'),
    path('collection', views.collection, name="collection"),
    path('collection/<str:name>', views.collectionsview, name="collection"),
    path('collection/<str:cname>/<str:pname>', views.product_details, name="product_details"),
    path('cart', views.cart_page, name="cart"),
    path('remove_cart/<str:cid>', views.remove_cart, name="remove_cart"),
    path('addtocart', views.add_to_cart, name="addtocart"),
    path('favorite', views.favorite_page, name="favorite"),
    path('favorite_viewpage', views.favorite_viewpage, name="favorite_viewpage"),
    path('remove_favorite/<str:fid>', views.remove_favorite, name="remove_favorite"),
    path('sale', views.sales_view, name="sale"),
    path('sale_product_price', views.sale_product_price_view, name="sale_product_price"),
    path('add_sale_product_price', views.add_sale_product_price_view, name="add_sale_product_price"),
    path('update_sale_product_price', views.update_sale_product_price_view, name="update_sale_product_price"),
    path('delete_sale_product_price/<int:id>', views.delete_sale_product_price_view, name="delete_sale_product_price"),
    path('show_sales_farmer_request', views.show_sales_farmer_request_view, name="show_sales_farmer_request"),
    path('approve_sales_farmer_request/<int:id>', views.approve_sales_farmer_request_view, name="approve_sales_farmer_request"),
    path('delete_sales_farmer_request/<int:id>', views.delete_sales_farmer_request_view, name="delete_sales_farmer_request"),
    path('show_farmer_detail', views.show_farmer_detail_view, name="show_farmer_detail"),
    path('delete_farmer_detail/<int:id>', views.delete_farmer_detail, name="delete_farmer_detail"),

    
    
    path('test', views.test, name="test"),
    path('Graph', views.graph_view, name="Graph"),
    path('search', views.search, name="search"),
]