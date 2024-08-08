# product.py
class Product:
    def do_something(self):
        pass

# concrete_product1.py
class ConcreteProduct1(Product):
    def do_something(self):
        print("ConcreteProduct1 doing something")

# concrete_product2.py
class ConcreteProduct2(Product):
    def do_something(self):
        print("ConcreteProduct2 doing something")

# creator.py
class Creator:
    def factory_method(self):
        pass

# concrete_creator.py
class ConcreteCreator(Creator):
    def factory_method(self):
        return ConcreteProduct1()  # or ConcreteProduct2()

# usage
creator = ConcreteCreator()
product = creator.factory_method()
product.do_something()
