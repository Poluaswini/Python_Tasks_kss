''' Develop a Python program to manage student marks for three subjects. Store the subject
names in a tuple, maintain unique student names in a set, and store each student’s marks
in a list inside a dictionary where the key is the student name. Create user-defined
functions to add a student with marks, display all student records, and calculate the average
marks of a student. Implement a recursive function to calculate the total marks from the list of
marks. The program should interact with the user through a simple menu. Also include
exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError
(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a
student name entered does not exist in the dictionary).'''

subjects=('maths','physics','science')
student=set()
student_marks={}

def recursive_total(marks, index):
    if index == len(marks):
        return 0
    return marks[index] + recursive_total(marks, index + 1)

def add_student():
    name=input("enter student name:")
    student.add(name)
    marks=[]
    try:
        for sub in subjects:
            mark=int(input(f"enter {sub} marks:"))
            marks.append(mark)
        student_marks[name]=marks
        print("added successfully")
    except ValueError:
        print("invalid enter")

def display_students():
    if not student_marks:
        print("there is no marks")
        return
    else:
        for name,marks in student_marks.items():
            print(name,":",marks)
def average_marks():
    try:
        name=input("enter student name:")
        if name not in student_marks:
            raise NameError
        marks=student_marks[name]
        total=recursive_total(marks,0)
        average=total/len(marks)
        print("total marks",total)
        print("average marks",average)
    except NameError:
        print("NameError: Student not found.")

    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")

    except TypeError:
        print("TypeError: Invalid data type in marks.")


while True:
    print("\n ....Menu...")
    print("1.Add student")
    print("2.display students")
    print("3.Average marks")
    print("4.exit")

    choice=int(input("enter your choice:"))

    if choice==1:
        add_student()
    elif choice==2:
        display_students()
    elif choice==3:
        average_marks()
    elif choice==4:
        print("exit")
        break
    else:
        print("invalid choice")
    


