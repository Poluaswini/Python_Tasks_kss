''' Q:A teacher stores student marks in a file marks.txt in the format:
Name Marks
Example:
Rahul 80
Anita 90
Ravi 75
Write a Python program to:
● Read the file
● Display all student records
● Calculate and display the average marks of the clas'''

file=open("marks.txt","w")
file.write("Rahul 80 \n")
file.write("Anita 90 \n")
file.write("Ravi 75 ")
file.close()

file=open("marks.txt", "r")
total=0
count=0
print("Student Records:")
for line in file:
    print(line.strip())
    data=line.split()      
    total += int(data[1])    
    count += 1              

file.close()

average=total / count
print("Average Marks:", average)



