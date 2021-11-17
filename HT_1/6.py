''' Task 6
Write a script to check whether a specified value is contained
in a group of values.'''

num = input('Enter number for check: ')
strSequenceNum = input('Enter numbers with symbol ",": ')
question = input('Numbers are list or tuple? Enter "l" or "t": ')
listNum = strSequenceNum.split(",")
def checkNum():
    if question == 'l':
        for i in listNum:
            if num == i:
                return True
        return False
    elif question == 't':
        tupleNum = tuple(listNum)
        for i in tupleNum:
            if num == i:
                return True
            return False
    else:
        print('Wrong answer!')

print(checkNum())
