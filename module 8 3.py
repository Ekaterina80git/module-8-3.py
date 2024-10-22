class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message

class Car:
    def __init__(self,model:str,vin:int,numbers:str):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self,vin_number):
        self.vin_number = vin_number
        if not isinstance(vin_number,int):
            raise IncorrectVinNumber('Не корректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Не верный диапазон для vin номера')
        return True

    def __is_valid_numbers(self,numbers):
        self.numbers = numbers
        if not isinstance(numbers,str):
            raise IncorrectCarNumbers('Не корректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Не верная длина номера')
        return True




try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')















