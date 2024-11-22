from django.urls import path
from . import views

urlpatterns = [
    path('checkout/',views.Checkout.as_view(),name='checkout'),
    path('checkout/',views.proceed_to_pay,name='checkout'),
]