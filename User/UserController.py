from flask import Blueprint
from flask import render_template, request, redirect, session
from User import UserService

bp = Blueprint('user', __name__, url_prefix='/')

userService = UserService.UserService()

def isAuthenticated():
    if 'user' in session:
        return True
    return False

## 회원 관리 관련 핸들러 ##
@bp.route('/viewRegister')
def viewRegister():
    return render_template('User/register.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@bp.route('/register', methods=['POST'])
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

@bp.route('/viewLogin')
def viewLogin():
    return render_template('User/login.html')

@bp.route('/login', methods=['POST'])
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

@bp.route('/viewUserInfo')
def viewUserInfo():
    if not isAuthenticated():
        return redirect('/')

    return render_template('User/userInfo.html')

@bp.route('/updateUserInfo', methods=['POST'])
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

@bp.route('/deleteUser')
def deleteUser():
    if not isAuthenticated():
        return redirect('/')
    id = session['user']['id']

    userService.deleteUser(id)

    session.clear()
    return redirect('/')