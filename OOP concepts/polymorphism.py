
class Employees:
    def __init__(self, firstname, lastname, income):
        self.firstname = firstname
        self.lastname = lastname
        self.income = income

    @property
    def email(self):
        return f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'


class Manager(Employees):
    budget = 10000

    def __init__(self, firstname, lastname, income):
        self.employee_list = []
        super().__init__(firstname, lastname, income)

    def add_employee(self, emp):
        self.employee_list.append(emp)
        return self.employee_list


class Director(Employees):
    budget = 30000

    def __init__(self, firstname, lastname, income):
        self.employee_list = []
        super().__init__(firstname, lastname, income)


class Sales(Employees):
    def __init__(self, firstname, lastname, income):
        super().__init__(firstname, lastname, income)

    # Polymorphism
    @property
    def email(self):
        return f'{self.firstname.lower()}.{self.lastname.lower()}@company_sales.com'


# Multiple inheritance
class TeamLeader(Director, Manager):
    def __init__(self, firstname, lastname, income, budget):
        super().__init__(firstname, lastname, income)


if __name__ == '__main__':
    s_man = Sales('Adi', 'Vasile', 300)
    d = Director('Mark', 'Wild', 1000)
    m = Manager('John', 'Clark', 3000)
    print(m.budget)
    print(s_man.email)
    print(d.email)
    tl = TeamLeader('Chris', 'Carrel', 2000, 5000)
    print(tl.add_employee(s_man))


