"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    for i in range(len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][-1]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    result = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        result.append(line.split(','))
        result[-1][-1] = int(result[-1][-1])
    input_file.close()
    return result


main()
