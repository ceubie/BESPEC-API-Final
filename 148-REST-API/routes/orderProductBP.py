from flask import Blueprint
from controllers.orderProductController import find_all


order_product_blueprint = Blueprint('order_products',__name__)

order_product_blueprint.route('/', methods=["GET"])(find_all)