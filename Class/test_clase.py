
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.cisco = age
        self.pay = pay
        self.job = job

    def getlastname(self):
        return self.name.split()[-1]

    def givecost(self, cost):
        self.pay *= (1.1 + cost)

    def __str__(self):
        return '<{0} => name:{1}, pay:{2}>'.format(self.__class__.__name__, self.name, self.pay)

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, job='Manager')

    def givecost(self, cost, meony=0.1):
        Person.givecost(self, cost + meony)

if __name__ == "__main__":
    hu = Person('hu chen', 30, 350000, 'network engine')
    fan = Person('fanwenling', 29, 60000, 'manager')
    ningning = Manager('chen shuning', 2, 90000)

    famliy = [hu, fan, ningning]
    for x in famliy:
        x.givecost(0.2)
        print(x)





