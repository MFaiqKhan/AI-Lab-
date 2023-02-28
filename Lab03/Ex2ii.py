# Write a python program to create a data file student.txt and append the message “Now we are
# AI students”s


def main():
    # open file for writing
    student_file = open('Lab03/student.txt', 'a')
    student_file.write("Now we are AI students")
    student_file.write('\n')
    # close the file
    student_file.close()

# call the main function
main()