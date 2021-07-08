class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'off'
        self._motor = Motor(cylinders=4)
        self._tank = Tank(10, 10)

    # Turns car on, if off only
    def turn_on(self):
        if self._state == 'off':
            print('*Car turns on*')
            self._state = 'on'

    # Turns car off, if on only
    def turn_off(self):
        if self._state == 'on':
            print('*Car turns off*')
            self._state = 'off'

    # Goes forward, if has gas in tank, else, turns off
    def forward(self, type='slow'):
        if self._state == 'on' and self._tank.current_fuel > 0:
            if type == 'slow':
                print('Brumm')
                self._motor.put_gas(2)
                self._tank.use_gas(2)
            elif type == 'fast':
                print('Bruuummmmm')
                self._motor.put_gas(4)
                self._tank.use_gas(4)
        elif self._state == 'off':
            print('Car is off')
        elif self._tank.current_fuel == 0:
            print('Out of gas\n*Turns off*')
            self._state = 'off'


# Unnecesary to overcomplicate,
# we only need to know that there is a motor thats needs gas
class Motor:
    def __init__(self, cylinders, fuel='gas'):
        self.cylinders = cylinders
        self.fuel = fuel
        self._temperature = 0.0

    def put_gas(self, cuantity):
        pass


# Car's gas tank, if ca goes forward,
# gas goes down
class Tank:
    def __init__(self, capacity, current_fuel):
        self.capacity = capacity
        self.current_fuel = current_fuel

    def use_gas(self, cuantity):
        if self.current_fuel - cuantity < 0:
            self.current_fuel = 0
        else:
            self.current_fuel -= cuantity


if __name__ == '__main__':
    mycar = Car('Logan', 'Renault', 'Gray')
    mycar.forward()
    mycar.turn_on()
    mycar.forward(type='fast')
    mycar.forward()
    mycar.turn_off()
    mycar.forward(type='fast')
    mycar.turn_on()
    mycar.forward(type='fast')
    mycar.forward(type='fast')
