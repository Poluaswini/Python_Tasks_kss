''' Q: A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results.'''

file=open("article.txt","w")
file.write("Word Counter Program")
file.close()

file=open("article.txt","r")
content=file.read()
print(content)
file.close()

lines=content.split("\n")
word=content.split()
characters=len(content)

print("number of lines",lines)
print("number of words",word)
print("number of characters",characters)