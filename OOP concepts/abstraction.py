from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod  # These abstract methods have to be implemented within the child class
    def email(self):
        pass

    @abstractmethod
    def hourly_income(self, working_days):
        pass


class Manager(Employee):
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def email(self):
        return f'{self.name}@company.com'

    def hourly_income(self, working_days):
        if working_days == 0:
            raise ValueError('must have at least 1 working day')
        return self.income/(8 * working_days)


if __name__ == '__main__':
    # Cannot instantiate the abstract class having abstract methods

    # e1 = Employee()

    m1 = Manager('Dan', 1000)
    mail = m1.email()
    print(mail)
    print(m1.hourly_income(23))

