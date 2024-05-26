from flask import Blueprint
from flask import render_template, request, redirect
from Product import ProductService

bp = Blueprint('product', __name__, url_prefix='/')

productService = ProductService.ProductService()

@bp.route('/products')
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