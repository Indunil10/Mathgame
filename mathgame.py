
try:
    import myPythonFunctions as m
    
    userName = input ("Enter your name :")
    
    userScore = int(m.getUserscore(userName))
    
    if userScore == -1:
        newUser = True
        userScore = 0
        
    else:
        newUser = False
        
    userChoice = 0
    
    while userChoice !='-1':
        
        userScore += m.genarateQuestions()
        print("Current score :",userScore)
        
        userchoices = input('Press Enter to continue or -1 to exit :')
        
    m.updateUserPoints(newUser, userName,str(userScore))
    
except Exception as e :
    print ("An unexpexted error occurres. program will be exited :")
    
    print('\n',e)

    