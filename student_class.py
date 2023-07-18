class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.age = None
        self.marks = None
    def setAge(self):
        self.age = int(input("Enter the age of student: "))
        print("Age updated")

    def setTestMarks(self):
        self.marks = float(input("Enter test mark of student: "))
        print("Mark Updated")
    
    def display(self):
        print("STUDEN DETAILS")
        print(f"Roll No: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

s1 = Student(name="Abc",rollno=10)

s1.display()
s1.setAge()
s1.setTestMarks()
s1.display()