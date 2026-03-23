from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Transport):
    def start_engine(self):
        return "Машина завелась"
    def stop_engine(self):
        return "Машина заглохла"

class Bicycle(Transport):
    def start_engine(self):
        return "Мотоцикл завёлся"
    def stop_engine(self):
        return "Мотоцикл заглох"

a = Car()
b = Bicycle()
print(a.start_engine(), a.stop_engine())
print(b.start_engine(), b.stop_engine())