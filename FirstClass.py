class Student:
    def __init__(self, name: str, rollno: int):
        self.name = name
        self.roll = rollno

    def showdata(self):
        print(f"the name is {self.name} and roll number is {self.roll}")


student1 = Student("sujan sapkota", 89)
student2 = Student("Reincarned", 16)

student1.showdata()
student2.showdata()
