class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Use the sorted function with a custom key to sort by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students = [
    Student("Hari", "001", 3.8),
    Student("Sneha", "002", 3.6),
    Student("Sam", "003", 4.0),
    Student("Tony", "004", 3.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
