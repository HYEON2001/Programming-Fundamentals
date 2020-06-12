class Sedan(Car):
    def upSpeed(self, value):
        self.speed +=value
    def getName(self):
        return  '{} (세단)'.format(self.name)

sedan = Sedan("아우디", 100)
print('이름: {}, 현재 속도: {}'.format(sedan.getName(), sedan.getSpeed()))
sedan.upSpeed(20)
print('이름: {}, 현재 속도: {}'.foramt(sedan.getName(), sedan.getSpeed()))
