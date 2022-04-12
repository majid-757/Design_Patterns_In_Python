class Builder:
    def getEngine(self):
        pass


    def getWhiles(self):
        pass


    def getBody(self):
        pass



class Benz(Builder):
    def getBody(self):
        body = Body()
        body.shape = 'suv'
        return body


    def getEngine(self):
        engine = Engine()
        engine.hp = 500
        return engine


    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel


class Bmw(Builder):
    def getBody(self):
        body = Body()
        body.shape = 'Sedan'
        return body


    def getEngine(self):
        engine = Engine()
        engine.hp = 340
        return engine


    def getWheel(self):
        wheel = Wheel()
        wheel.size = 18
        return wheel





class Wheel:
    size = None


class Body:
    shape = None


class Engine:
    hp = None









