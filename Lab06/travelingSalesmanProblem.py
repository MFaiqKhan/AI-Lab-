# import itertools # for permutations function , which generates all possible permutations of a list

def generate_permutations(values, current_permutation=None, remaining_values=None, acc=None):
    if current_permutation is None:
        current_permutation = []
        print("Init: current_permutation =", current_permutation)
    if remaining_values is None:
        remaining_values = values.copy()
        print("Init: remaining_values =", remaining_values)

        # yield is like return, but it returns a generator object instead of a value , e.g. <generator object generate_permutations at 0x0000020D0F4F4C80> 
        # means that the function generate_permutations returned a generator object at memory address 0x0000020D0F4F4C80
        # this is useful because we can iterate over the generator object to get the permutations one by one, without having to store all of them in memory at once

    if acc is None:
        acc = []

    if not remaining_values: # if remaining_values is empty
        print("Yielding: current_permutation =", current_permutation)
        # yield current_permutation 
        acc.append(current_permutation)
    else:
        for i, value in enumerate(remaining_values): # enumerate returns a tuple (index, value) for each value in the list remaining_values
            print(f"Loop: i={i}, value={value}, remaining_values={remaining_values}")
            new_remaining_values = remaining_values[:i] + remaining_values[i+1:] 
            # remove the value at index i from the list remaining_values and store the result in new_remaining_values, e.g. if remaining_values = [1,2,3] and i = 1 then new_remaining_values = [1,3] why is it done like this? because we want to remove the value at index i from the list remaining_values and store the result in new_remaining_values , so we need to concatenate the first part of remaining_values (from index 0 to index i-1) with the second part of remaining_values (from index i+1 to the end of the list) , its useful to do it like this because we dont have to iterate over the list remaining_values to remove the value at index i , we just concatenate the first part of remaining_values with the second part of remaining_values and we get a new list without the value at index i
            print("Updated: new_remaining_values =", new_remaining_values)
            print("Updated: current_permutation + [value] =", current_permutation + [value])
            # yield from generate_permutations(values, current_permutation + [value], new_remaining_values) # 
            generate_permutations(values, current_permutation + [value], new_remaining_values, acc) #


            # yield from is used to delegate the generation of permutations to another generator object 
            # (the one returned by generate_permutations) , current_permutation + [value] is the new permutation that will be yielded by the generator object returned by generate_permutations

    return acc


# Imagine we have values = [1, 2, 3]. Here's a step-by-step explanation of the control flow:

# Note: [ Recursion tree ](https://en.wikipedia.org/wiki/Recursion_(computer_science)#Recursive_tree) is a useful concept to understand recursion.
# Note: Recursion Tree means a tree of recursive calls , e.g. if a function calls itself 3 times then the recursion tree will have 3 levels , 
# the first level is the first call to the function , the second level is the second call to the function , 
# the third level is the third call to the function , the fourth level is the fourth call to the function , etc.

# The first call to generate_permutations has current_permutation=[] and remaining_values=[1, 2, 3].
# The loop iterates through each value in remaining_values. For the first value (1), new_remaining_values becomes [2, 3]. 
# The function is called recursively with current_permutation=[1] and remaining_values=[2, 3].
# The loop in the recursive call iterates through the updated remaining_values. For the first value (2), new_remaining_values becomes [3].
#  The function is called recursively with current_permutation=[1, 2] and remaining_values=[3].
# The loop in this recursive call iterates through the remaining value (3). 
# Since there are no more values left in remaining_values after removing 3, the base case is reached, and the current permutation [1, 2, 3] is appended to the acc list.
# The control goes back to the previous call in the recursion tree, where current_permutation=[1, 2] and remaining_values=[3]. 
# The loop continues with the next value, but there are no more values left, so the control goes back to the previous call with current_permutation=[1] and remaining_values=[2, 3].
# The loop in this call continues with the next value (3), and new_remaining_values becomes [2]. 
# The function is called recursively with current_permutation=[1, 3] and remaining_values=[2].
# This process continues until all permutations are generated and appended to the acc list.
#  The control flow in the version with yield is similar, but instead of appending the permutations to a list, the generator function yields them one by one.

def tsp_bruteforce(distances):
    n = len(distances)
    cities = list(range(1, n)) # list of cities to visit , e.g. if n = 4 then cities = [1,2,3] as we dont need to visit city 0 because we start and end at city 0
    
    min_cost = float('inf') # float('inf') is a special value that represents infinity , we use it to initialize min_cost to infinity
    min_permutation = None

    #  will this generate perumations one by one or all at once?  one by one , 
    # because generate_permutations returns a generator object and we are iterating over it so how the code works ?  
    # the for loop will call next() on the generator object returned by generate_permutations and the generator object will yield the next permutation , 
    # so the for loop will get the permutations one by one and store them in the variable permutation , then it will execute the body of the for loop for each permutation
    
    print("Starting brute-force TSP:")
    for permutation in generate_permutations(cities):
        print("permutation = " , permutation)
        cost = distances[0][permutation[0]] + distances[permutation[-1]][0] # cost of the path from city 0 to city permutation[0] and from city permutation[-1] to city 0
        # permutation[-1] is the last element in the tuple permutation , e.g. if permutation = (1,2,3) then permutation[-1] = 3
        # e.g: if permutation = (1,2,3) then permutation[0] = 1 and permutation[-1] = 3 so distances[0][permutation[0]] = distances[0][1] and distances[permutation[-1]][0] = distances[3][0]
        # so cost = distances[0][1] + distances[3][0] = cost of the path from city 0 to city 1 and from city 3 to city 0 
        # it shows that we start at city 0 and end at city 0 , so we dont need to visit city 0 because we start and end at city 0
        
        for i in range(len(permutation) - 1):
            cost += distances[permutation[i]][permutation[i + 1]] 
            # why len of permutation is -1 ? as it doesnt contain city 0 then why we need to subtract 1 from its length ? 
            # becuase length is the number of elements in the tuple , e.g. if permutation = (1,2,3) then len(permutation) = 3 , 
            # so len(permutation) - 1 = 3 - 1 = 2 , so the for loop will iterate from 0 to 1 , so i will be 0 and 1 ,
            # so permutation[i] will be permutation[0] and permutation[1] , so permutation[i] will be 1 and 2 ,`
            # so permutation[i + 1] will be permutation[0 + 1] and permutation[1 + 1] , so permutation[i + 1] will be 2 and 3 ,
            # so distances[permutation[i]][permutation[i + 1]] will be distances[1][2] and distances[2][3] ,
            # so cost += distances[permutation[i]][permutation[i + 1]] will be cost += distances[1][2] and cost += distances[2][3] ,
            # so cost = cost + distances[1][2] + distances[2][3] = cost of the path from city 1 to city 2 and from city 2 to city 3
            # so we visit city 1 then city 2 then city 3 then we go back to city 0 , so we visit all cities except city 0`
        
        if cost < min_cost:
            min_cost = cost # hamiltonian cycle cost
            min_permutation = permutation # hamiltonian cycle path
            
            # weight of the hamiltonian cycle is the sum of the weights of the edges in the hamiltonian cycle 
            # here we calculate the weight of the hamiltonian cycle and store it in min_cost
    
    min_permutation = (0,) + tuple(min_permutation) + (0,) # add 0 at the beginning and at the end of the tuple min_permutation , e.g. if min_permutation = (1,2,3) then (0,) + tuple(min_permutation) + (0,) = (0,1,2,3,0) 
    # shows that we start at city 0 and end at city 0 , so we dont need to visit city 0 because we start and end at city 0
    # min_permutation shows the order of cities to visit , e.g. if min_permutation = (1,2,3) then we visit city 1 then city 2 then city 3 then we go back to city 0 , so we visit all cities except city 0
    return min_cost, min_permutation

# Example usage
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = tsp_bruteforce(distances)
print("\nResult:")
print("Minimum cost:", cost)
print("Path:", path)


""" 
In the context of the Traveling Salesman Problem (TSP), a Hamiltonian cycle is a closed loop that visits each vertex (city) 
exactly once and returns to the starting vertex. The weight of a Hamiltonian cycle in TSP refers to the total cost or distance of traversing the cycle. 
The objective of TSP is to find the Hamiltonian cycle with the minimum weight (i.e., the shortest possible route) that visits each city exactly once and returns to the starting city.

In other words, a Hamiltonian cycle is a path that visits each city in a graph without visiting any city more than once and returns to the starting city. 
The weight of the cycle is the sum of the distances between consecutive cities in the cycle, including the distance between the last city and the starting city. 
The goal of TSP is to find the Hamiltonian cycle with the lowest weight, which represents the shortest route to visit all cities and return to the starting point.
"""


