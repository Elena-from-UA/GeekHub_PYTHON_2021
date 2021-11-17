''' Task 3
Write a script to sum of the first n positive integers.'''

numberForSum = int(input("Enter n: "))
i = 1
totalSum = 0
while i <= numberForSum:
    totalSum = totalSum + i
    i += 1
print(totalSum)
