''' Task 4
Write a script to concatenate N strings.'''

countStr = int(input("Enter n: "))
i = 1
concatStr = ''
while i <= countStr:
    inputStr = input("Enter string: ")
    concatStr = concatStr + inputStr
    i += 1
print(concatStr)
