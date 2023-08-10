from django.urls import path

from catalog.views import contacts, index, ProductDetailView, blog_list_view


urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('list/', blog_list_view, name='catalog_list'),
]
