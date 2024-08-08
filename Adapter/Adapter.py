# target.py
class Target:
    def request(self):
        pass

# adaptee.py
class Adaptee:
    def adaptee_method(self):
        print("Adaptee doing something")

# adapter.py
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.adaptee_method()

# usage
adaptee = Adaptee()
adapter = Adapter(adaptee)
adapter.request()
