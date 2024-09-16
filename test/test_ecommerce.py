# import unittest
#
# from ecommerce.ecommerce import Market, Product, Customer, Cart
#
#
# class TestMarket(unittest.TestCase):
#     def setUp(self):
#         self.market = Market()
#         self.customer_1 = Customer(name="Jane", last_name="Doe")
#         self.customer_2 = Customer(name="John", last_name="Doe")
#         self.customer_3 = Customer(name="John", last_name="Doe")
#
#     def test_customer_id_generation(self):
#         self.assertEqual(self.customer_1.id, "0001")
#         self.assertEqual(self.customer_2.id, "0002")
#
#     def test_customer_email_generation(self):
#         Customer._emails_taken = ['john.doe@example.com']+[f"john.doe_{i:02d}@example.com" for i in range(1, 100)]
#
#
#         self.assertEqual(self.customer_1.email, "jane.doe@example.com")
#         self.assertEqual(self.customer_2.email, "john.doe@example.com")
#         self.assertEqual(self.customer_3.email, "john.doe_01@example.com")
#         with self.assertRaises(ValueError):
#             customer_4 = Customer(name="John", last_name="Doe")
#
#
#     def test_add_product_to_cart(self):
#         customer = Customer(name="John", last_name="Doe")
#         cart = Cart(customer=customer)
#         product_1 = Product(name="Laptop", price=1000)
#         product_2 = Product(name="Mouse", price=20)
#
#         cart.add_product(product_1, 2)
#         cart.add_product(product_2, 1)
#         self.assertEqual(cart.total_price, 2020)
#
#     def test_remove_product_from_cart(self):
#         customer = Customer(name="John", last_name="Doe")
#         cart = Cart(customer=customer)
#         product_1 = Product(name="Laptop", price=1000)
#         product_2 = Product(name="Mouse", price=20)
#
#         cart.add_product(product_1, 1)
#         cart.add_product(product_2, 1)
#         cart.remove_product(product_1, 1)
#         self.assertEqual(cart.total_price, 20)
#
#         cart.remove_product(product_1, 1)
#         self.assertEqual(cart.total_price, 20)
#         self.assertEqual(cart.products, [Product(name='Mouse', price=20, stock=0)])
