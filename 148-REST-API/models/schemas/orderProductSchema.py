from . import ma
from marshmallow import Schema, fields

class OrderProductSchema(Schema):
    order_id = fields.Int()
    product_id = fields.Int()

order_product_schema = OrderProductSchema()
orders_products_schema = OrderProductSchema(many=True) 