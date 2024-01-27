# Multilevel Inheritance
class User:
    def __init__(self, name, salary, profession):
        self.name = name
        self.salary = salary
        self.profession = profession

    def register_employee(self):
        print(f'Registering user {self.name}')


class Manager(User):
    def __init__(self, name, salary, profession, responsible_sector):
        super().__init__(name, salary, profession)
        self.responsible_sector = responsible_sector

    def define_sector(self, sector):
        print(f'Defining sector to {sector}')


# Usage example
user1 = User('Camila', 50000, 'Software Analyst')
manager1 = Manager('Roberta', 80000, 'Manager', 'Project Management')
