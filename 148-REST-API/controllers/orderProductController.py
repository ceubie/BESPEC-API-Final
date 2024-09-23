from flask import request, jsonify
from models.schemas.orderProductSchema import orders_products_schema
from services import orderProductService
from cache import cache


@cache.cached(timeout=30)
def find_all():
    all_order_products = orderProductService.find_all()

    result = orders_products_schema.dump(all_order_products)

    return jsonify(result), 200