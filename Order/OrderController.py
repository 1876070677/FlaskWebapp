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

    sequenceId = orderService.createOrder(id, username, phone, email, address, cart, session['finalTotalPrice'])

    return redirect(f'/viewOrderDetail?seq={sequenceId}')

@bp.route('/viewOrderDetail')
def viewOrderDetail():
    if not us.isAuthenticated():
        return redirect('/')
    sequenceId = request.args.get('seq', type=int)
    if sequenceId is None:
        return redirect('/viewOrderHistory')
    sequence = orderService.permissionCheck(session['user']['id'], sequenceId)

    if not sequence:
        return redirect('/')

    orderDetails = orderService.getOrderDetails(sequence['id'])

    return render_template('Order/orderDetails.html', sequence=sequence, orderDetails=orderDetails)

@bp.route('/viewOrderHistory')
def viewOrderHistory():
    if not us.isAuthenticated():
        return redirect('/')

    sequence = orderService.getSequences(session['user']['id'])

    return render_template('Order/orderHistory.html', sequence=sequence)
