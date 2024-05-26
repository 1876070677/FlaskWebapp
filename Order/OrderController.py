from flask import Blueprint
from flask import render_template, request, redirect, session
from User import UserController as us
from Cart import CartService
from Order import OrderService

cartService = CartService.CartService()
orderService = OrderService.OrderService()

bp = Blueprint('order', __name__, url_prefix='/')
@bp.route('/viewOrder')
def viewOrder():
    if not us.isAuthenticated():
        return redirect('/')
    if 'cart' not in session or len(session['cart']) == 0:
        return render_template('Cart/cart.html', message='Cart is empty!')

    return render_template('Order/order.html')
    # cart = cartService.sessionToCartDict(session['cart'])
    # orderService.createOrder(cart)

@bp.route('/createOrder', methods=['POST'])
def createOrder():
    if not us.isAuthenticated():
        return redirect('/')
    if 'cart' not in session or len(session['cart']) == 0:
        return render_template('Cart/cart.html', message='Cart is empty!')

    id = request.form.get('id').strip()
    username = request.form.get('username').strip()
    phone = request.form.get('phone').strip()
    email = request.form.get('email').strip()
    address = request.form.get('address').strip()

    cart = cartService.sessionToCartDict(session['cart'])

    orderService.createOrder(id, username, phone, email, address, cart)

    return render_template('Order/viewOrderDetail')