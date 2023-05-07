def tower_of_hanoi(n, source, target, auxiliary, depth=0):
    indent = '    ' * depth
    print(f"{indent}Entering tower_of_hanoi({n}, {source}, {target}, {auxiliary})")
    
    if n == 1:
        print(f"{indent}  Disk 1 moved from {source} to {target}")
    else:
        tower_of_hanoi(n - 1, source, auxiliary, target, depth + 1)
        print(f"{indent}  Disk {n} moved from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, target, source, depth + 1)

    print(f"{indent}Exiting tower_of_hanoi({n}, {source}, {target}, {auxiliary})")

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')



""" 
The given code is a Python implementation of the Tower of Hanoi problem using recursion. 
The Tower of Hanoi is a classic problem that demonstrates the power of recursion in solving problems that can be broken down into smaller problems of the same kind.

The function tower_of_hanoi takes the following parameters:

n: The number of disks
source: The source peg
target: The target peg
auxiliary: The auxiliary (helper) peg
depth: The depth of the current recursive call (default is 0)
The function uses recursion to solve the problem with the following steps:

Move the top n - 1 disks from the source peg to the auxiliary peg, using the target peg as a helper.
Move the n-th disk from the source peg to the target peg.
Move the n - 1 disks from the auxiliary peg to the target peg, using the source peg as a helper.
The base case is when n == 1, in which case the function simply prints the move of the single disk from the source peg to the target peg.

The depth parameter is used to visualize the recursion, by indenting the function calls according to their depth in the call stack.

Here is the output of the given code with n = 3:

Entering tower_of_hanoi(3, A, C, B)
    Entering tower_of_hanoi(2, A, B, C)
        Entering tower_of_hanoi(1, A, C, B)
          Disk 1 moved from A to C
        Exiting tower_of_hanoi(1, A, C, B)
      Disk 2 moved from A to B
        Entering tower_of_hanoi(1, C, B, A)
          Disk 1 moved from C to B
        Exiting tower_of_hanoi(1, C, B, A)
    Exiting tower_of_hanoi(2, A, B, C)
  Disk 3 moved from A to C
    Entering tower_of_hanoi(2, B, C, A)
        Entering tower_of_hanoi(1, B, A, C)
          Disk 1 moved from B to A
        Exiting tower_of_hanoi(1, B, A, C)
      Disk 2 moved from B to C
        Entering tower_of_hanoi(1, A, C, B)
          Disk 1 moved from A to C
        Exiting tower_of_hanoi(1, A, C, B)
    Exiting tower_of_hanoi(2, B, C, A)
Exiting tower_of_hanoi(3, A, C, B)


This output shows the recursive nature of the problem and how the function calls itself with smaller subproblems until the base case is reached. 
The solution to the Tower of Hanoi problem with 3 disks involves moving the disks in the following order:

Disk 1 from A to C
Disk 2 from A to B
Disk 1 from C to B
Disk 3 from A to C
Disk 1 from B to A
Disk 2 from B to C
Disk 1 from A to C
The time complexity of this recursive solution is O(2^n), where n is the number of disks.


"""


# dry run
# n = 3
# tower_of_hanoi(3, 'A', 'C', 'B')
#     else:
#         tower_of_hanoi(2, 'A', 'B', 'C')  
#             else:
#                 tower_of_hanoi(1, 'A', 'C', 'B')
#                     print(f"Disk 1 moved from A to C")
#             print(f"Disk 2 moved from A to B")
#             tower_of_hanoi(1, 'C', 'B', 'A')
#                 print(f"Disk 1 moved from C to B")
#         print(f"Disk 3 moved from A to C")
#         tower_of_hanoi(2, 'B', 'C', 'A')
#             else:
#                 tower_of_hanoi(1, 'B', 'A', 'C')
#                     print(f"Disk 1 moved from B to A")
#            print(f"Disk 2 moved from B to C")
#            tower_of_hanoi(1, 'A', 'C', 'B')
#                 print(f"Disk 1 moved from A to C")

# EXSPLAIN THE CODE
# The function tower_of_hanoi() is called with n = 3, source = 'A', target = 'C', secondary = 'B'
# The function checks if n == 1, which is false, so it goes to the else statement
# The function calls itself with n = 2, source = 'A', target = 'B', secondary = 'C'
# The function checks if n == 1, which is false, so it goes to the else statement
# The function calls itself with n = 1, source = 'A', target = 'C', secondary = 'B'
# The function checks if n == 1, which is true, so it prints "Disk 1 moved from A to C"
# The function returns to the previous call, which prints "Disk 2 moved from A to B" ? 
# The function calls itself with n = 1, source = 'C', target = 'B', secondary = 'A'
