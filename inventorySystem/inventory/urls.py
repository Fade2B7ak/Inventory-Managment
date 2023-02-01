from django.urls import path
from .views import inventory_list, per_product_view, add_product, delete_product, update_product


urlpatterns = [
    path("", inventory_list, name="inventory_list"),
    path("product/<int:pk>", per_product_view, name="per_product"),
    path("add_product/", add_product, name="add_product"),
    path("delete/<int:pk>", delete_product, name="del_product"),
    path("update/<int:pk>", update_product, name="update_product"),
]
