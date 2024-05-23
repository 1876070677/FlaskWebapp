from flask import Flask, render_template, request, redirect, session
from User import UserService, User
from Product import ProductService, Product
import random
app = Flask(__name__)
app.secret_key="ABCD"

userService = UserService.UserService()
productService = ProductService.ProductService()

category = ['outer', 'top', 'bottom', 'acc']

for i in range(1000):
    productService.addProduct(Product.Product(i, '[3단기장/Free/인생데님] 로킷 데님 와이드핏 롱 워싱 데님 팬츠 1color', random.randrange(10000, 20000), '', random.choice(category), random.randrange(50, 100)))

user = User.User('admin', 'admin', 'admin', '1111', '', '')
userService.addUser(user)

@app.route('/')
def hello():
    return render_template('welcome.html')

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
    user = User.User(id, password, username, phone, email, address)

    userService.addUser(user)

    session['id'] = id
    session['username'] = username
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
    if not userService.checkIdPw(id, password):
        return render_template('User/login.html', message='id와 pw를 확인해주세요')

    user = userService.getUser(id)
    session['id'] = user.id
    session['username'] = user.name
    return redirect('/')

@app.route('/products')
def getProducts():
    kind = request.args.get('kind')
    if kind is None:
        return redirect('/products?kind=all')
    if kind == 'all':
        products = productService.getAllProducts()
    else:
        products = productService.getProductsByKind(kind)

    return render_template('Product/productList.html', productList=products)

@app.route('/addCart', methods=['POST'])
def addCart():
    productId = request.form.get('productId')
    quantity = request.form.get('quantity')

    product = productService.getProductById(productId)

    if product.quantity < quantity:
        message = '구매 가능 수량을 초과하였습니다'
    return redirect("/")