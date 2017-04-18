import os
import random 

def getUserscore (userName):
    try:            
        input=open('userScores.txt','r')
        for line in input:
            content=line.split(',')
            if content[0]==userName:
                input.close()
                return content[1]
        input.close()
        return "-1"
    except IOError:
        print("There is no file named 'userScores.txt'\n a new file will be created")
        input=open('userScores.txt','w')
        input.close()
        return "-1"
    
    
def updateUserPoints(newUser,userName,score):
      
    if newUser:
        input=open('userScores','a')
        
        input.write('\n + userName + ',' + score')
        
        input.close()
    else:
        input = open('userScores.txt', 'r')
        output = open('userScores.tmp', 'w')
    for line in input:
    
        content = line.split(',')
        if content[0] == userName:
            content[1] = score
            line = content[0] + ', ' + content[1] + '\n'

        output.write(line)
    input.close()
    output.close()

    remove('userScores.txt')
    rename('userScores.tmp', 'userScores.txt')
        
def genarateQuestions():
    operandList = [0,0,0,0,0]
    operatorList = ['','','','']
    operatorDict = {1:'+',2:'-',3:'*',4:'**'}
    
    for x in range (0,5):
        operandList[x] = randit(1,9)
        
    for y in range(0,4):
        if y >0 and operatorList[y-1] != '**':
            opertor=operatorDict[randint(1,5)]
            
        else:
            operator = operatorDict[randint(1,4)]
            
        operatorList[y] = operator
        
    questionString =str(operandList[0])
    
    for z in range (1,5):
        questionString = questionString + operatorList[z-1] + str(operandList[z])
        
    result = eval(questionString)
        
    questionString = questionString.replace('**','^')
        
    print(questionString)
        
    userResult = input('Answer : ')
    
    while True:
        try:
            if int(userResult)== result:
                print("Your answer is correct")
                return 1
            else:
                print("Your Answer is incorrect \n the correct answer is :",result)
                
                return 0
        except Exception as e:
            print("You should enter a number please try again.")
            
            userResult = input('Answer : ')
            
        
        