'''Q:Advanced Simulation System
Scenario:
Simulate exam results and generate reports.
Task:
● Generate random marks using random
● Store in NumPy array
● Convert to Pandas DataFrame
● Use OOP to represent Student
● Use conditions + loops to assign grades
● Save report to file
● Handle errors using try-except
● Use math module for statistics'''
import random
import math
import numpy as np
import pandas as pd


# OOP - Student class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"


try:
    # Generate random marks
    marks = []

    for i in range(5):
        marks.append(random.randint(0, 100))

    print("Random Marks:", marks)

    # Convert to NumPy array
    marks_array = np.array(marks)
    print("NumPy Array:", marks_array)

    # Create students
    students = []

    for i in range(5):
        student = Student("Student" + str(i + 1), marks_array[i])
        students.append(student)

    # Store results
    names = []
    student_marks = []
    grades = []

    for student in students:
        names.append(student.name)
        student_marks.append(student.marks)
        grades.append(student.get_grade())

    # Convert to Pandas DataFrame
    df = pd.DataFrame({
        "Name": names,
        "Marks": student_marks,
        "Grade": grades
    })

    print("\nStudent Report:")
    print(df)

    # Statistics using math module
    average = math.fsum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("\nStatistics:")
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)

    # Save report to file
    with open("exam_report.txt", "w") as file:

        file.write("EXAM REPORT\n")
        file.write("====================\n")
        file.write(df.to_string(index=False))
        file.write("\n\nStatistics\n")
        file.write("Average: " + str(average) + "\n")
        file.write("Highest: " + str(highest) + "\n")
        file.write("Lowest: " + str(lowest) + "\n")

    print("\nReport saved successfully.")

except Exception as e:
    print("Error:", e)