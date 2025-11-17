
class Student:
    def __init__(self,name, age, grade):
        self.grade= grade
        self.name= name
        self.age= age
    
    def change_age(self,new_age):
        self.age= new_age

        

    
patrik=Student('patrik', 13,  8)

print(patrik.name)
print(patrik.grade)
patrik.change_age(17)
print(patrik.age)
