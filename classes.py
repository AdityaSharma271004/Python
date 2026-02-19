class employee: #class
    name= "aditya"          #class attribute
    profession = "youtuber" #class attribute
    salary = "1.5cr"        #class attribute
    language = "python"     #class attribute

    def getInfo(self):
        print(f"the language is {self.language} and salary is {self.salary}")
    
    @staticmethod #if you don't want to pass the self argument so you declare your method or function as @staticmethod.
    def greet():
        print("good morning sir..")


object = employee()
object.language = "javascript" #instance object -> which takes the preference as  first.
# print(object.name,object.profession,object.salary,object.language)  
object.greet()
object.getInfo()  
# employee.getInfo(object) #same working as line no-13.