
# swap 4 vars function

def swap4vars(a, b, c, d):
    [a, b, c, d] = [d, c, b, a]
    return [a, b, c, d]

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))
d = int(input('Enter a number: '))

print(swap4vars(a, b, c, d))