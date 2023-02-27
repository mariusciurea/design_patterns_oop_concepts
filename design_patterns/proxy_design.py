import logging


class Manager:
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def email(self):
        return f'{self.name.lower()}@company.com'

    def hourly_income(self, working_days):
        return self.income/(8 * working_days)


class ProxyEmployee:
    def __init__(self):
        self.employee = Manager('Marius', 3000)
        logging.basicConfig(level=logging.INFO, filename='log.log', filemode='w',
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def email(self):
        logging.info(f'Manager email: {self.employee.email()}')
        self.employee.email()


if __name__ == '__main__':
    emp = ProxyEmployee()
    emp.email()

