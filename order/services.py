from .models import Cart, CartItem, Order, OrderItem
from django.db import transaction

class OrderService:
    @staticmethod
    def create_order(cart_id: int, user_id: int) -> Order:
        with transaction.atomic():
            cart = Cart.objects.get(id=cart_id)
            cart_items = cart.items.select_related('product').all()
                
            total_price = sum(item.product.price * item.quantity for item in cart_items)
            order = Order.objects.create(user_id=user_id, total_price=total_price)
            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                    total_price=item.product.price * item.quantity
                )
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)
            cart_items.delete()
            return order
        
    @staticmethod
    def cancel_order(order , user):
        if user.is_staff:
            order.status = Order.CANCELED
            order.save()
    
        if order.user != user:
            raise Exception( {'status': 'You do not have permission to cancel this order.'} )
        
        if order.status == Order.DELIVERED:
            raise Exception( {'status': 'Delivered orders cannot be cancelled.'} )
        
        order.status = Order.CANCELED
        order.save()
        return order
            