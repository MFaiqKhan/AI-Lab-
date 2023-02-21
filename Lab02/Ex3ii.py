# Loop that counts from 0 to 100

for i in range(101):
    print(i)

# Multiplication table using a loop

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

# Output numbers 1 to 10 backwards using a loop

for i in range(10, 0, -1):
    print(i)

# Loop that counts all even numbers to 10

for i in range(0, 11, 2):
    print(i)


# Loop that sums the numbers from 100 to 200

sum = 0
for i in range(100, 201):
    sum += i
print(sum)

