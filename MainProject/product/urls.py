from django.urls import path
from . import views
urlpatterns = [
    path('brand-list/',views.brand_list,name='brand_list'),
    path('add-product/',views.AddProduct.as_view(),name='add_product')
]

