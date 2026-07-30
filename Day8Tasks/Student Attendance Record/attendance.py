'''Q: A teacher wants to store student attendance in a file named attendance.txt. Write a
Python program that takes a student name as input and appends it to the file. Then
display the contents of the file.'''
student_name=input("enter name:")
file=open("attendence.txt","a")
file.write(student_name+"\n")
file.close()

file=open("attendence.txt","r")
print("\n Total attendance")
print(file.read())
file.close()
