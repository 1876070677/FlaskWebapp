from flask import Flask, render_template, request, redirect, session
from User import UserService, User
from Product import ProductService, Product
app = Flask(__name__)
app.secret_key="ABCD"

userService = UserService.UserService()
productService = ProductService.ProductService()

product1 = Product.Product(1, '[3단기장/Free/인생데님] 로킷 데님 와이드핏 롱 워싱 데님 팬츠 1color', 20400, '바지', 'bottom', 100)
product2 = Product.Product(2, '[3단기장/Free/인생데님] 로킷 데님 와이드핏 롱 워싱 데님 팬츠 1color', 20400, '바지', 'bottom', 100)
product3 = Product.Product(3, '[3단기장/Free/인생데님] 로킷 데님 와이드핏 롱 워싱 데님 팬츠 1color', 20400, '바지', 'bottom', 100)
productService.addProduct(product1)
productService.addProduct(product2)
productService.addProduct(product3)

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
    id = request.form.get('id')
    password = request.form.get('password')
    username = request.form.get('username')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')

    ## Validate ##
    if id == '' or password == '' or username == '' or phone == '':
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
    id = request.form.get('id')
    password = request.form.get('password')

    ## Validate ##
    if id == '' or password == '':
        return render_template('User/login.html', message='id와 pw를 모두 입력해주세요')

    ## 아이디 비밀번호 확인 ##
    if not userService.checkIdPw(id, password):
        return render_template('User/login.html', message='id와 pw를 확인해주세요')

    user = userService.getUser(id)
    session['id'] = user.id
    session['username'] = user.name
    return redirect('/')

@app.route('/kind')
def getProductsOfKind():
    kind = request.args.get('kind')
    products = productService.getProductsOfKind(kind)

    return render_template('Product/productList.html', productList=products)