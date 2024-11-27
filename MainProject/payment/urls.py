from django.urls import path
from . import views
urlpatterns = [
    path('confirm-payment/',views.confirm_payment,name='confirm payment'),
]