from marshmallow import fields, validate
from schemas import ma

# Define the shopping cart 
class ShoppingCartSchema(ma.Schema):
    id = fields.Integer(required=False) # id is autogenerated
    customer_id = fields.Integer(required=True)
    products = fields.Nested("ProductIdSchema", many=True)

class UpdateProductQuantitySchema(ma.Schema):
    quantity = fields.Integer(required=True, validate=validate.Range(min=0))

# Create instances of the schema
shopping_cart_schema = ShoppingCartSchema()
shopping_carts_schema = ShoppingCartSchema(many=True)
update_product_quantity_schema = UpdateProductQuantitySchema()