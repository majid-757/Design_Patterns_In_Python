
class A:
    def __init__(self, name, format):
        self.name = name
        self.format = format


class B:
    def edit(self, file):
        if file.format == 'json':
            print(f'Editing Json File .... {file.name}')

        elif file.format == 'xml':
            print(f'Editing Xml File .... {file.name}')

        else:
            raise ValueError('Sorry.....')




a1 = A('majid', 'json')
b1 = B()

b1.edit(a1)
