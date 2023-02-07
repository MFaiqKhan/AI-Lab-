
# create a program that perform following tasks

# Introduction to the program

def main():
    
    print("Hello, welcome to the program")
    print("This program will calculate the area of a rectangle")
    print("Please enter the length and width of the rectangle")
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("The area of the rectangle is: ", area)

    # use text editor to create a file called "rectangle.md"
    open("rectangle.md", "w")
    # write the program into the file through list and for loop
    for i in range(1, 11):
        print("Hello, welcome to the program", file=open("rectangle.md", "a"))
        print("This program will calculate the area of a rectangle", file=open("rectangle.md", "a"))
        print("Please enter the length and width of the rectangle", file=open("rectangle.md", "a"))
        print("Enter the length: ", file=open("rectangle.md", "a"))
        print("Enter the width: ", file=open("rectangle.md", "a"))
        print("The area of the rectangle is: ", file=open("rectangle.md", "a"))

    #use confitional statement to check if the area is greater than 100
    if area > 100:
        print("The area is greater than 100")
    else:
        print("The area is less than 100")

    
print(main())