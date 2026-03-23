# Function to assign grade
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

students = {}

# Input data for 5 students
for i in range(1, 6):
    name = input(f"Enter name of student {i}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

# Find topper
topper = max(students, key=students.get)

# Calculate class average
average = sum(students.values()) / len(students)

print("\nStudent Grades:")
for name, marks in students.items():
    grade = get_grade(marks)
    print(name, "- Marks:", marks, "- Grade:", grade)

print("\nTopper:", topper, "with", students[topper], "marks")
print("Class Average:", average)