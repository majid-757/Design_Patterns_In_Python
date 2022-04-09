from abc import ABC, abstractmethod



class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass


    @abstractmethod
    def call_coupe(self):
        pass

#---------------------------------------------
class Benz(Car):
    def call_suv(self):
        return Gla()


    def call_coupe(self):
        return Cls()

#---------------------------------------------
class Bmw(Car):
    def call_suv(self):
        return X1()


    def call_coupe(self):
        return M2()








