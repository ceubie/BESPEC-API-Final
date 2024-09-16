from database import db, Base

customer_cart = db.Table(
    'customer_cart',
    Base.metadata,
    db.Column('customer_id', db.ForeignKey('customers.id'),primary_key=True),
    db.Column('product_id', db.ForeignKey('products.id'),primary_key=True)
)

   
cart = db.relationship("Product", secondary='customer_cart', back_populates="customer_cart")