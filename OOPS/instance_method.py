class Student:
    school_name = 'Hogwarts'
    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        print(self.age)
    def om1(self):
        print(self.name, self.roll_no, self.age)
    def om2(self, points):
        print(f'Points for {self.name}: {points}')
        
ob1 = Student('Harry', 1, 15)
ob2 = Student('Ron', 2, 16)
ob3 = Student('Hermione', 3, 16)
#Accessing instance methods using class reference.
Student.om1(ob1)
Student.om1(ob2)
Student.om1(ob3)
#Accessing instance methods using object reference.
ob1.om2(100)
ob2.om2(98)
ob3.om2(99)
