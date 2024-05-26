from flask import Blueprint
from flask import render_template, request, redirect, session
from User import UserController as us
from Cart import CartService

cartService = CartService.CartService()

bp = Blueprint('order', __name__, url_prefix='/')
@bp.route('/createOrder')
def createOrder():
    if not us.isAuthenticated():
        return redirect('/')
    if 'cart' not in session or len(session['cart']) == 0:
        return render_template('Cart/cart.html', message='Cart is empty!')

    cart = cartService.sessionToCartDict(session['cart'])
    # orderService.createOrder(cart)