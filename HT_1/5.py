''' Task 5
 Write a script to convert decimal to hexadecimal'''

decimalNum = input("Enter decimal numbers with ',':")
decimalNumList = decimalNum.split(',')
decimalNumList = [int(i) for i in decimalNumList]
hexList = []

for i in decimalNumList:
    hexNum = hex(i)
    hexList.append(hexNum)
print(hexList)
