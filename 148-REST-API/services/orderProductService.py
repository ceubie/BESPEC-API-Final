from database import db 
from models.orderProduct import order_product 
from sqlalchemy import select 



def find_all():
    query = select(order_product)
    all_order_products = db.session.execute(query).scalars().all()

    return all_order_products