from django.urls import path
from products import views as products_view


urlpatterns = [
    path('', products_view.getProducts, name="products"),
    path('<str:pk>/reviews/', products_view.createProductReview, name="create-review"),
    path('top/', products_view.getTopProducts, name="top-products"),
    path('<str:pk>/', products_view.getProduct, name="product"),
]