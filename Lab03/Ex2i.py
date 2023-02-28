# You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number of
# cities from the keyboard and store the data in a file in the order in which they’re entered.

def main():
    # open file for writing
    cities_file = open('Lab03/cities.txt', 'w')

    # get number of cities
    num_cities = int(input('How many cities do you want to enter? '))

    # get data and write it to the file
    for count in range(1, num_cities + 1): 
        # range(1, 4) = [1, 2, 3] 
        #  range(1, 5) = [1, 2, 3, 4], 
        # range(1, 5 + 1) = [1, 2, 3, 4, 5]

        # get the city data
        print('Enter data for city #', count, sep='') # sep is the separator between the arguments passed to print()
        # here sep is playing the role of a space
        name = input('Name: ')
        population = int(input('Population: '))
        mayor = input('Mayor: ')

        # write the data as a record to the file
        cities_file.write(name + ' ' + str(population) + ' ' + mayor)
        
        # write a newline character to the file
        cities_file.write('\n')


    # close the file
    cities_file.close()


# call the main function
main()
