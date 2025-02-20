# Создаем класс Car
class Car:
 
    # создаем атрибуты класса
    name = "c200"
    make = "mercedez"
    model = 2008
 
    # создаем методы класса
    def start(self):
        print ("Заводим двигатель")
 
    def stop(self):
        print ("Отключаем двигатель")
car_b = Car()
car_b.start()
print(car_b.model)
