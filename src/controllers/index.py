import pymysql
from src.controllers.customer.customer_controller import Customer
from src.controllers.customer.address_controller import Address
from src.controllers.order.order_controller import Order
from src.controllers.order.details_controller import Details
from src.controllers.product.product_controller import Product
from src.controllers.product.categories_controller import Category
from src.controllers.product.movements_controller import Movement
from src.controllers.supplier.products_controller import Product as SupplierProduct
from src.controllers.supplier.suppliers_controller import Supplier


class DataHandler():
    def __init__(self):
        self._customer = Customer()
        self._customer_address = Address()
        self._order = Order()
        self._order_details = Details()
        self._product = Product()
        self._product_categories = Category()
        self._product_movements = Movement()
        self._supplier = Supplier()
        self._supplier_product = SupplierProduct()
