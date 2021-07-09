class Plane:

    # Constructor
    def __init__(self, brand, model, safe):
        self._brand = brand
        self._model = model  # Protected  - Can only be acceded by this class and it's subclasses
        self.__safe = safe  # Private    -

    # Brand management, getter, setter, deleter
    @property
    def brand(self):
        print('--> Using  Getter')
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        print('--> Using  Setter')
        if type(new_brand) == str and len(new_brand.replace(' ', '')) > 0:
            self._brand = new_brand
            print(f'New Brand = {self._brand}')
        else:
            print('Error on new brand. must be str and not empty')

    @brand.deleter
    def brand(self):
        print('--> Deleting Brand')
        del self._brand

    # Model management, getter, setter, deleter
    @property
    def model(self):
        print('--> Using  Getter')
        return self._model

    @model.setter
    def model(self, new_model):
        print('--> Using  Setter')
        if type(new_model) == str and len(new_model.replace(' ', '')) > 0:
            self._model = new_model
            print(f'New Model = {self._model}')
        else:
            print('Error on new model. must be str and not empty')

    @model.deleter
    def model(self):
        print('--> Deleting Model')
        del self._model

    # Safe management, getter, setter
    @property
    def safe(self):
        print('--> Using  Getter')
        return self.__safe

    @safe.setter
    def safe(self, new_safe):
        print('--> Using  Setter')
        if ' ' in new_safe:
            raise ValueError('Password cant include whitespace')
        if type(new_safe == str) and len(new_safe) >= 6:
            self.__safe = new_safe
            print(f'New password = {self.__safe}')
        else:
            print('Error, password must have 6 characters minimum')


p = Plane(brand='A', model='B', safe='qwerty')

# Testing brand
print(p.brand)
p.brand = 'Avianca'
del p.brand
p.brand = 'VivaAir'
print(p.brand)

# Testing model
print(p.model)
p.model = 'Boeing 771'
del p.model

# Testing sage
print(p.safe)
# p.safe = '   '            # this cant be done
# p.safe = 'asd lajsdbfn'   # this neither
p.safe = 'asdlajsdbfn'
