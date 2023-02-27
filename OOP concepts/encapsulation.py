
class Employee:
    amount = 1.02

    def __init__(self, firstname, lastname, position, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.__pay = pay

    def raise_amount(self):
        return self.__pay * self.amount

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, income):
        if self.position == 'manager':
            if income < 100:
                raise ValueError('In case of a manager, the income has to be at least 100!')
            self.__pay = income


if __name__ == '__main__':
    emp = Employee('Dan', 'Chivu', 'manager',  100)
    print(emp.raise_amount())
    # print(emp.__pay)  # cannot access the private attribute __pay
    emp.pay = 120
    print(emp.pay)
    print(emp.raise_amount())