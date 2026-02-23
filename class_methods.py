
'''
class Employee:
    a = 1
    
    @classmethod  #@classmethod enables the class attribute not instance attribute
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

e = Employee()
e.a  = 45
e.show()      '''  


#property decorater


class Student:
    pass
    
    @property
    def name(self):
        return self.sname


    @name.setter
    def name(self,value):
        self.sname = value    

s = Student()
s.name = "aditya"
print(s.name)


