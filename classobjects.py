class student:
  def __init__(self, rollno, name, marks, age):
    self.rollno = rollno
    self.name = name
    self.marks = marks
    self.age = age

s1 = student(1, "Ali", 50, 21)
s2 = student(2, "Ahmad", 45, 22)
s3 = student(3, "Arham", 48, 21)


print("Rollno:", s1.rollno)
print("Name:", s1.name)
print("Marks:", s1.marks)
print("Age:", s1.age)


print("Rollno:", s2.rollno)
print("Name:", s2.name)
print("Marks:", s2.marks)
print("Age:", s2.age)


print("Rollno:", s3.rollno)
print("Name:", s3.name)
print("Marks:", s3.marks)
print("Age:", s3.age)
