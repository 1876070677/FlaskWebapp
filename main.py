from flask import Flask, render_template, request, redirect, session
from User import  UserController
from Product import ProductController
from Cart import CartController
from flask_cors import CORS

app = Flask(__name__)
app.secret_key="ABCD"
CORS(app)

app.register_blueprint(UserController.bp)
app.register_blueprint(ProductController.bp)
app.register_blueprint(CartController.bp)

## 메인페이지 ##
@app.route('/')
def hello():
    return render_template('welcome.html')