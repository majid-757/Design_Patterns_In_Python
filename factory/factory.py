
# class A:
#     def __init__(self, name, format):
#         self.name = name
#         self.format = format


# class B:
#     def edit(self, file):
#         edit = self._get_edit(file)
#         return edit(file)

#     def _get_edit(self, file):

#         def edit(self, file):
#             if file.format == 'json':
#                 return self.json_edit

#             elif file.format == 'xml':
#                 return self.xml_edit

#             else:
#                 raise ValueError('Sorry.....')

#     def json_edit(self, file):
#         print(f'Editing Json File .... {file.name}')


#     def xml_edit(self, file):
#         print(f'Editing Xml File .... {file.name}')


# a1 = A('majid', 'json')
# b1 = B()

# b1.edit(a1)



from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def edit(self):
        pass



class Json(Product):
    def edit(self):
        return 'Editing Json File ....'



class Xml(Product):
    def edit(self):
        return 'Editing Xml File ....'



