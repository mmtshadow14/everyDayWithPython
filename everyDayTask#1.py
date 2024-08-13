
print("hello !!!")

print("please enter your list of nums and when you are done pls enter (done) . ")

listOfNum=[]
keepGettingNum=True
while keepGettingNum == True:

    number=input()
    if number == 'done':
        keepGettingNum=False
    else :
        listOfNum.append(int(number))


maxNum=int(input("now please enter the max number you want to see ."))

minNum=int(input("now please enter the min number you want to see ."))

resultList=[]

for num in listOfNum:

    if num<=maxNum and num>=minNum :

        resultList.append(num)

print(resultList)

