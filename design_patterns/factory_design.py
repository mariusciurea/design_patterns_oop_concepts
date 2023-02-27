from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
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
        return self.income/(8 * working_days)


class Director(Employee):
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def email(self):
        return f'{self.name}@company.com'

    def hourly_income(self, working_days):
        return (self.income + 200) / (8 * working_days)


class EmployeeFactoryPattern:
    @staticmethod
    def get_employee(empl_type):
        if empl_type == "Manager":
            return Manager('default', 1000)
        elif empl_type == 'Director':
            return Director('default', 2000)
        raise ValueError('not a good type')


if __name__ == '__main__':
    empl_type = input('Choose: ')
    employee = EmployeeFactoryPattern.get_employee(empl_type)
    print(employee.hourly_income(22))
