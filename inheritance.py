class Employee:
    company = "aditya tech services"
    salary = 12345
    def show(self):
        
        print(f"the name of the employee is {self.company}and the salary is {self.salary}")


class Programmer(Employee):
    
    language = "python"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language}")

a = Employee()
b = Programmer()
b.show()
b.showLanguage()