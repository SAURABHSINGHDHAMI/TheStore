from django.urls import path
from orders import views as orders_view

urlpatterns = [
    path('add/', orders_view.addOrderItems, name="orders-add"),
    path('myorders/', orders_view.getMyOrders, name="myorders"),
    path('<str:pk>/', orders_view.getOrderById, name="user-order"),
    path('<str:pk>/pay/', orders_view.updateOrderToPaid, name="pay"),
]