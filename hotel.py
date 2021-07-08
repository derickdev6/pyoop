class Hotel:

    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes


hotel = Hotel(50, 20)
print('Se crea hotel con max cap 50 y estacionamientos 20')
hotel.anadir_huespedes(33)
print('Se hace checkin de 33 y out de 10')
hotel.checkout(10)
print(f'Ocupacion de hotel= {hotel.ocupacion_total()}')
