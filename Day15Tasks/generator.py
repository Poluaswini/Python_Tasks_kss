'''Q:Generator-based Log Reader
Scenario:
A large log file needs to be processed.
Task:
● Create a generator to read file line by line
● Use loop to process logs
● Use condition to filter errors
● Count occurrences using a dictionary'''
def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


error_count = {}

for log in read_logs("logs.txt"):

    if "ERROR" in log:
        error = log.split(":")[1].strip()

        if error in error_count:
            error_count[error] += 1
        else:
            error_count[error] = 1


print("Error occurrences:")

for error, count in error_count.items():
    print(error, ":", count)