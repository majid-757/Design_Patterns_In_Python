
class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()

        return self._instance


class Dj(metaclass=Singleton):
    pass 



d1 = Dj()
d2 = Dj()

print(id(d1))
print(id(d2))

