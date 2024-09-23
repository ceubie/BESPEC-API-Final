from database import db 
from models.product import Product
from models.customer import Customer
from models.order import Order
from models.orderProduct import order_product
from models.cart import customer_cart
from sqlalchemy import select 
from datetime import date

def get_customer(customer_id):
    customer = db.session.query(Customer).get(customer_id)
    if not customer:
        raise ValueError("customer not found")
    return customer

def add_items_to_cart(customer_id, cart_data):

    customer = get_customer(customer_id)
    products_ids = cart_data['product_ids']

    customer = db.session.query(Customer).get(customer_id)
    if not customer:
        raise ValueError("Customer not found")

    for product_id in products_ids:
        product = db.session.query(Product).get(product_id)
        if not product:
            raise ValueError("Product id: {product_id}, not found.")
        if product not in customer.cart:
            customer.cart.append(product)
            print(product.id, product.product_name, product.price)
       
    db.session.commit()

def remove_item_from_cart(customer_id, cart_data):
    customer = get_customer(customer_id)
    print("customer", customer)
    product_ids = cart_data['product_ids']

    products = db.session.query(Product).filter(Product.id.in_(product_ids)).all()

    for product in products:
        if product in customer.cart:
            customer.cart.remove(product)
    db.session.commit()

def view_cart(customer_id):
    query = (
        select(Product.id, Product.product_name, Product.price)
        .select_from(customer_cart.join(Product, customer_cart.c.product_id == Product.id))
        .where(customer_cart.c.customer_id == customer_id)
    )

    all_cart_items = db.session.execute(query).fetchall()
    print(f"Query result: {all_cart_items}")  


    cart_items = []
    for row in all_cart_items:
        item = {
            "id": row.id,
            "name": row.product_name,
            "price": row.price
        }
        cart_items.append(item)
    return cart_items


def empty_cart(customer_id):
    customer = get_customer(customer_id)
    customer.cart.clear()
    db.session.commit()

def place_order(customer_id):
    customer = get_customer(customer_id)

    if not customer.cart:
        raise ValueError ("Cart is empty")
    
    new_order = Order(customer_id=customer.id, date=date.today())

    for product in customer.cart:
        new_order.products.append(product)
    
    customer.cart.clear()
    
    db.session.add(new_order)

    db.session.commit()
    return new_order