from flask import Flask, render_template, request, redirect, session
from User import UserService, User
app = Flask(__name__)
app.secret_key="ABCD"

userService = UserService.UserService()

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

@app.route('/register')
def register():
    id = request.args.get('id')
    password = request.args.get('password')
    username = request.args.get('username')
    phone = request.args.get('phone')
    email = request.args.get('email')
    address = request.args.get('address')

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

@app.route('/login')
def login():
    id = request.args.get('id')
    password = request.args.get('password')

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