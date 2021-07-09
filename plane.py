class Plane:
    def __init__(self, brand, model, safe):
        self._brand = brand
        self._model = model  # Protected  - Can only be acceded by this class and it's subclasses
        self.__safe = safe  # Private    -

    def get_brand(self):
        print('Using Getter')
        return self._brand

    def get_model(self):
        print('Using Getter')
        return self._model

    def get_safe(self):
        print('Using Getter')
        return self.__safe

    def set_brand(self, new_brand):
        if type(new_brand) == str and len(new_brand.replace(' ', '')) > 0:
            self._brand = new_brand
        else:
            print('Error on new brand. must be str and not empty')

    def set_model(self, new_model):
        if type(new_model) == str and len(new_model.replace(' ', '')) > 0:
            self._model = new_model
        else:
            print('Error on new model. must be str and not empty')


p = Plane(brand='A', model='B', safe='qwerty')
print(p.get_brand())
print(p.get_model())
print(p.get_safe())

p.set_brand('')
p.set_model('   ')
print(p._model)
# print(p.__safe)       # This doesn't work
# This works, we have to add _<ClassName> before the property name
print(p._Plane__safe)
