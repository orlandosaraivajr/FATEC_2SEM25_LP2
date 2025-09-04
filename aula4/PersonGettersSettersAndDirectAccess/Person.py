# Person class

class Person():

    def __init__(self, name, salary):
        self.name = name
        self.salario = salary
 
    # Allow the caller to retrieve the salary
    def getSalary(self): 
        return self.salario

    # Allow the caller to set a new salary
    def setSalary(self, salary):
        self.salario = salary
