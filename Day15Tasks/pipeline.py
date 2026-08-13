'''Q:Smart Data Processing Pipeline
Scenario:
A system processes numeric data from file.
Task:
● Read numbers from a file
● Use NumPy for calculations (mean, std)
● Convert results to Pandas DataFrame
● Use exception handling for bad data
● Use a generator to stream data
● Apply decorator to measure execution time'''
import numpy as np
import pandas as pd
import time


def execution_time(func):
    def wrapper():
        start = time.time()

        result = func()

        end = time.time()
        print("Execution time:", end - start, "seconds")

        return result

    return wrapper


def read_numbers(filename):
    with open(filename, "r") as file:
        for line in file:
            try:
                yield float(line.strip())
            except ValueError:
                print("Invalid data:", line.strip())


@execution_time
def process_data():

    numbers = []

    for number in read_numbers("numbers.txt"):
        numbers.append(number)

    arr = np.array(numbers)

    mean = np.mean(arr)
    std = np.std(arr)

    print("Mean:", mean)
    print("Standard Deviation:", std)

    result = pd.DataFrame({
        "Mean": [mean],
        "Standard Deviation": [std]
    })

    print(result)


process_data()