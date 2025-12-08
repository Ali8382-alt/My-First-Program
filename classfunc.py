class student:
  def __init__(self, rollno, name, marks, age):
    self.rollno = rollno
    self.name = name
    self.marks = marks
    self.age = age

  def info(self):
        print("Rollno:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Age:", self.age)

s1 = student(1, "Ali", 50, 21)
s2 = student(2, "Ahmad", 45, 22)
s3 = student(3, "Arham", 48, 21)
  
  
s1.info()