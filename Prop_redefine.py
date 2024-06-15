class Vehicle:
    def __init__(self, owner, _model, _engine_power, _color):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color
        self._COLOR_VARIANTS = ['Blue', 'Red', 'Green', 'Black', 'White']

    def get_model(self):
        return f'Модель: {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in [i.lower() for i in self._COLOR_VARIANTS]:
            self._color = new_color
            print(f'Цвет изменен на {self._color}')
        else:
            print(f'Нельзя изменить цвет на {new_color}')


class Sedan(Vehicle):

    def __init__(self, owner, _model, _engine_power, _color):
        super().__init__(owner=owner, _model=_model, _engine_power=_engine_power, _color=_color)
        self._PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
