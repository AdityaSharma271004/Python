# create a class 'employee' and add salary and increament properties to it.

class Employee:
    salary = 12345
    increment = 20
     
    @property 
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increament = ((salary / self.salary ) -1) *100

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 20
print(e.increment)
