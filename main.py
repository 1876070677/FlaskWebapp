from flask import Flask, render_template, request, redirect, session
from User import UserService
from Product import ProductService
from Cart import CartService
from flask_cors import CORS

app = Flask(__name__)
app.secret_key="ABCD"
CORS(app)

userService = UserService.UserService()
productService = ProductService.ProductService()
cartService = CartService.CartService()

def isAuthenticated():
    if 'user' in session:
        return True
    return False

## 메인페이지 ##
@app.route('/')
def hello():
    return render_template('welcome.html')

## 회원 관리 관련 핸들러 ##
@app.route('/viewRegister')
def viewRegister():
    return render_template('User/register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    id = request.form.get('id').strip()
    password = request.form.get('password').strip()
    username = request.form.get('username').strip()
    phone = request.form.get('phone').strip()
    email = request.form.get('email').strip()
    address = request.form.get('address').strip()

    ## Validate ##
    if len(id) == 0 or len(password) == 0 or len(username) == 0 or len(phone) == 0:
        return render_template('User/register.html', message='필수 정보를 입력해주세요 (id, pw, username, phone)')
    ## 중복 확인 ##
    if userService.checkUser(id):
        return render_template('User/register.html', message='중복된 id를 입력하였습니다')

    user = userService.addUser(id, password, username, phone, email, address)

    session['user'] = user
    return redirect('/')

@app.route('/viewLogin')
def viewLogin():
    return render_template('User/login.html')

@app.route('/login', methods=['POST'])
def login():
    id = request.form.get('login_id').strip()
    password = request.form.get('login_password').strip()
    ## Validate ##
    if len(id) == 0 or len(password) == 0:
        return render_template('User/login.html', message='id와 pw를 모두 입력해주세요')

    ## 아이디 비밀번호 확인 ##
    user = userService.login(id, password)
    if not user:
        return render_template('User/login.html', message='id와 pw를 확인해주세요')

    session['user'] = user
    return redirect('/')

@app.route('/viewUserInfo')
def viewUserInfo():
    if not isAuthenticated():
        return redirect('/')

    return render_template('User/userInfo.html')

@app.route('/updateUserInfo', methods=['POST'])
def updateUserInfo():
    if not isAuthenticated():
        return redirect('/')
    id = request.form.get('id').strip()
    password = request.form.get('password').strip()
    username = request.form.get('username').strip()
    phone = request.form.get('phone').strip()
    email = request.form.get('email').strip()
    address = request.form.get('address').strip()

    ## Validate
    if len(id) == 0 or len(password) == 0 or len(username) == 0 or len(phone) == 0:
        return render_template('User/userInfo.html', message='필수 정보를 입력해주세요 (pw, username, phone)')

    user = userService.updateUserInfo(id, password, username, phone, email, address)
    session.clear()

    session['user'] = user
    return redirect('/viewUserInfo')

@app.route('/deleteUser')
def deleteUser():
    if not isAuthenticated():
        return redirect('/')
    id = session['user']['id']

    userService.deleteUser(id)

    session.clear()
    return redirect('/')

@app.route('/products')
def getProducts():
    """
    :return: first (데이터 시작), end(데이터 끝), pageFirst(페이징의 첫번째), pageEnd(페이징의 마지막), currentPage(현재 페이지), category(종류)
    """
    category = request.args.get('category', default='all')
    page = request.args.get('page', type=int, default=1)
    if category is None:
        return redirect('/products?kind=all')
    if page is None:
        page = 1
    products, pageFirst, pageEnd, end, = productService.getProductsByCategory(category, page)

    return render_template('Product/productList.html', currentPage=page, category=category, pageFirst=pageFirst, pageEnd=pageEnd, end=end, productList=products)

@app.route('/viewCart')
def viewCart():
    if not isAuthenticated():
        return redirect('/')
    if 'cart' not in session:
        session['cart'] = {}
    return render_template('/Cart/cart.html')

def manageCart():
    if 'cart' not in session:
        session['cart'] = {}
        return {}
    cart = session['cart']
    updateCart = {}
    for product in cart:
        updateCart[int(product)] = cart[product]

    return updateCart

@app.route('/addCart', methods=['POST'])
def addCart():
    if not isAuthenticated():
        return redirect('/')
    productId = request.form.get('productId', type=int)
    quantity = request.form.get('quantity', type=int)

    if ('cart') not in session:
        session['cart'] = {}

    cart, finalTotalPrice = cartService.addCart(session['cart'], productId, quantity)
    session.pop('cart')
    session['cart'] = cart
    session['finalTotalPrice'] = finalTotalPrice

    return redirect("/viewCart")

@app.route('/updateQuantity', methods=['POST'])
def updateQuantity():
    if not isAuthenticated():
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

@app.route('/deleteProduct', methods=['POST'])
def deleteProduct():
    if not isAuthenticated():
        return redirect('/')
    productId = request.form.get('productId', type=int)

    cart, finalTotalPrice = cartService.deleteProduct(session['cart'], productId)

    session.pop('cart')
    session['cart'] = cart

    session['finalTotalPrice'] = finalTotalPrice

    return redirect("/viewCart")
