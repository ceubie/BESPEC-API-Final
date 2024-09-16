from . import ma
from marshmallow import Schema, fields

class CartSchema(ma.Schema):
    customer_id = fields.Int(required=True)
    product_ids = fields.List(fields.Int(), required=True) #able to accept list of products
    product_id = fields.Int()

    class Meta:
        fields = ('customer_id','product_ids', 'product_id')

cart_schema = CartSchema()
carts_schema = CartSchema(many=True) 