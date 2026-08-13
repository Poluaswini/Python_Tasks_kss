'''Q:Basic File Logger
Scenario:
A system logs user actions.
Task:
● Take user input
● Store logs in a file
● Use loop to allow multiple entries
● Handle file errors using exception handling'''
try:
    with open("user_logs.txt", "a") as file:

        while True:
            action = input("Enter user action (or 'exit' to stop): ")

            if action.lower() == "exit":
                break

            file.write(action + "\n")
    print("Logs saved successfully.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", e)