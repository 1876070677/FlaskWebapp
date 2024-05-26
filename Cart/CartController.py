from flask import Blueprint
from flask import render_template, request, redirect, session
from Cart import CartService
from User import UserController as us

bp = Blueprint('cart', __name__, url_prefix='/')

cartService = CartService.CartService()

@bp.route('/viewCart')
def viewCart():
    if not us.isAuthenticated():
        return redirect('/')
    if 'cart' not in session:
        session['cart'] = {}
    return render_template('/Cart/cart.html')

@bp.route('/addCart', methods=['POST'])
def addCart():
    if not us.isAuthenticated():
        return redirect('/')
    productId = request.form.get('productId', type=int)
    quantity = request.form.get('quantity', type=int)

    if 'cart' not in session:
        session['cart'] = {}

    cart, finalTotalPrice = cartService.addCart(session['cart'], productId, quantity)
    session.pop('cart')
    session['cart'] = cart
    session['finalTotalPrice'] = finalTotalPrice

    return redirect("/viewCart")

@bp.route('/updateQuantity', methods=['POST'])
def updateQuantity():
    if not us.isAuthenticated():
        return redirect('/')
    productId = request.form.get('productId', type=int)
    quantity = request.form.get('quantity', type=int)

    if 'cart' not in session:
        session['cart'] = {}

    cart, finalTotalPrice = cartService.updateQuantity(session['cart'], productId, quantity)

    session.pop('cart')
    session['cart'] = cart

    session['finalTotalPrice'] = finalTotalPrice

    return redirect("/viewCart")

@bp.route('/deleteProduct', methods=['POST'])
def deleteProduct():
    if not us.isAuthenticated():
        return redirect('/')
    productId = request.form.get('productId', type=int)

    cart, finalTotalPrice = cartService.deleteProduct(session['cart'], productId)

    session.pop('cart')
    session['cart'] = cart

    session['finalTotalPrice'] = finalTotalPrice

    return redirect("/viewCart")