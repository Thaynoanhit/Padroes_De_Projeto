# subject.py
class Subject:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

# observer.py
class Observer:
    def update(self, message):
        pass

# concrete_subject.py
class ConcreteSubject(Subject):
    pass

# concrete_observer.py
class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")

# usage
subject = ConcreteSubject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.register_observer(observer1)
subject.register_observer(observer2)

subject.notify_observers("Hello, world!")