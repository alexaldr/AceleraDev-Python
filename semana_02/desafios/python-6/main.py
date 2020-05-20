from abc import ABCMeta, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(metaclass=ABCMeta):
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self._department = department  # _ = protected, __ = private

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8

    def get_departament(self):
        return self._department.name
    
    def set_departament(self, name):
        self._department.name = name


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self._sales = 0

    def calc_bonus(self):
        return self._sales * 0.15
    
    def get_sales(self):
        return self._sales
    
    def put_sales(self, value):
        self._sales += value
