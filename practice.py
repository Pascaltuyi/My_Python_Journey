customer: str = "susan"
pizza_base: str = "Thin"
pizza_size: int = 12
topping: str = "chees"
extra_cheese: str = "mozarrera"
price: float = 14.2

print(f"Recevied order from {customer}")
print(f"The pizza base is called {pizza_base}")
print(f"the pizza size is {pizza_size}")
print(f"and Added a topping of {topping}")
print(f"He ordered extra {extra_cheese}")
print(f"The price is {price}")

order_detailes: str = f"""
Recevied order from {customer}
The pizza base is called {pizza_base}
the pizza size is {pizza_size}
and Added a topping of {topping}
He ordered extra {extra_cheese}
"""
print(order_detailes)


