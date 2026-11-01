
import csv


students = [
    {"Roll No": "101", "Name": "Alice", "Department": "CSE", "Mark": 86},
    {"Roll No": "102", "Name": "Bob", "Department": "ECE", "Mark": 92},
    {"Roll No": "103", "Name": "Charlie", "Department": "ME", "Mark": 78}
]

course = ("Python",4)
print("Course tuple:", course)
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

with open("Students.csv", "w", newline="") as file:
    fields = ["Roll No", "Name", "Department", "Mark"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)




print("\n---Records from CSV---")
with open("Students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Roll No"], row["Name"], row["Department"], row["Mark"])
