"""
URL configuration for qubits project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html")),
    path('',TemplateView.as_view(template_name="index.html"),name = '#'),
    path('product/',include('product.urls')),
    path('accounts/',include('accounts.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),  # Home page
    path('shop/', TemplateView.as_view(template_name='shop.html'), name='shop'),  # Shop page
    path('product/', TemplateView.as_view(template_name='single-product-details.html'), name='single-product-details'),  # Product details page
    path('checkout/', TemplateView.as_view(template_name='checkout.html'), name='checkout'),  # Checkout page
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),  # Blog page
    path('blog/', TemplateView.as_view(template_name='single-blog.html'), name='single-blog'),  # Single blog page
    path('regular-page/', TemplateView.as_view(template_name='regular-page.html'), name='regular-page'),  # Regular page
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),  # Contact page

]



from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)