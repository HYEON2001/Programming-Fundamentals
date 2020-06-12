class Car :
    def __init__(self, name='', speed=0):
        self.name = name
        self.speed = speed

    def getName(self):
        return '{} 자동차'.format(self.name)

    def getSpeed(self):
        return  '{}km/h'.format(self.speed)

car1 = Car("아우디")
car2 = Car("벤츠", 30)

print("{}의 현재 속도는 {}입니다.".format(car1.getName(), car1.getSpeed()))
print("{}의 현재 속도는 {}입니다.".format(car2.getName(), car2.getSpeed()))
