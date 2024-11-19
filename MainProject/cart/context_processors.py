from .models import Cart
from django.contrib.auth.models import User
from product.models import ProductImages
def cart_items(request):
    if request.user.is_authenticated:
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        cart_data = []
        for item in cart_items:
            product_image = ProductImages.objects.filter(product=item.product).first()
            cart_data.append({
                'product': item,
                'image': product_image,
            })
        return {'cart_items': cart_data,
                'total_cart_item': len(cart_data)}
    return {'cart_items': []}