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



class Wheel:
    size = None


class Body:
    shape = None


class Engine:
    hp = None









