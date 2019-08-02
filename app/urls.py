from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, HomePageView
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("products/", ProductListView.as_view(), name='product_list'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name='product_delete'),
    path("products/<int:pk>/add/", views.inventory_add, name='inventory_add'),
    path("products/<int:pk>/less/", views.inventory_remove, name='inventory_remove'),
    path("new/", ProductCreateView.as_view(), name='product_new'),
]
