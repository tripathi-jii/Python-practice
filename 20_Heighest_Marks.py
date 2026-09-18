# Program to add and find heighest marks of students

students = {
    "Rahul": 85,
    "Aman": 92,
    "Rohit": 78,
    "Vikas": 95,
    "Ankit": 88
}

highest_student = max(students, key = students.get)

print("Highest Scorer:", highest_student)
print("Marks:", students[highest_student])