from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Product:
    name: str
    price: float
    stock: int = 0


@dataclass
class Customer:
    name: str
    last_name: str
    id: str = field(init=False)
    email: str = field(init=False)
    _number_of_customers: ClassVar[int] = 0
    _emails_taken: ClassVar[list[str]] = []

    def __post_init__(self):
        self.name = self.name.lower()
        self.last_name = self.last_name.lower()
        self.email = self._set_email()
        Customer._number_of_customers += 1
        self.id = f"{Customer._number_of_customers:04d}"

    def _set_email(self, number: int = 0):
        if number:
            email = f"{self.name}.{self.last_name}_{number:02d}@example.com"
        else:
            email = f"{self.name}.{self.last_name}@example.com"

        if number > 99:
            raise ValueError("Too many customers with the same name and last name")
        elif email in Customer._emails_taken:
            return self._set_email(number + 1)
        else:
            Customer._emails_taken.append(email)
            return email


@dataclass
class Cart:
    customer: Customer
    products: list[Product] = field(default_factory=list)
    total_price: float = 0

    def add_product(self, product: Product, quantity: int):
        self.products.extend([product] * quantity)
        self.total_price += product.price * quantity

    def remove_product(self, product: Product, quantity: int):

        products_output = []
        for item in self.products:
            if item != product or quantity == 0:
                products_output.append(item)
            else:
                quantity -= 1
                self.total_price -= product.price

        self.products = products_output


@dataclass
class Order:
    id: str
    customer: Customer
    products: list[Product]
    total_price: float


@dataclass
class Market:
    orders: list[Order] = field(default_factory=list)
    total_sales: float = 0

    def checkout(self, cart: Cart):

        for product in cart.products:
            if product.stock == 0:
                raise ValueError(f"{product.name} is out of stock")
            product.stock -= 1

        order = Order(id=f"{len(self.orders) + 1:03d}", customer=cart.customer, products=cart.products,
                      total_price=cart.total_price)
        self.total_sales += order.total_price

        self.orders.append(order)
