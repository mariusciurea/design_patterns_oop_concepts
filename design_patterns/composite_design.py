from abc import ABC, abstractmethod


class IEmployee(ABC):
    @abstractmethod
    def email(self):
        pass

    @abstractmethod
    def hourly_income(self):
        pass


class Manager(IEmployee):
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def email(self):
        return f'{self.name}@company.com'

    def hourly_income(self):
        return self.income/(8 * 22)


class Director(IEmployee):
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def email(self):
        return f'{self.name}@company.com'

    def hourly_income(self):
        return (self.income + 200) / (8 * 22)


class CompositeEmployee(IEmployee):
    def __init__(self):
        self.child_employees = []

    def add_employees(self, empl):
        self.child_employees.append(empl)

    def email(self):
        for item in self.child_employees:
            print(item.email())

    def hourly_income(self):
        for item in self.child_employees:
            print(item.hourly_income(22))


if __name__ == '__main__':
    m1 = Manager('Dani', 1000)
    d1 = Director('Maria', 3000)
    c_empl = CompositeEmployee()
    c_empl.add_employees(m1)
    c_empl.add_employees(d1)
    print(c_empl.child_employees)
    c_empl.email()
