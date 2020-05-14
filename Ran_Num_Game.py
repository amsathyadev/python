print("WELCOME to the NUMBER GAME")
import random
GUESS = random.randint(1,100)
RANDOM = GUESS
COUNT =1

        
while(COUNT<=5):
       
    if(COUNT == 5 and NUM!=GUESS and GUESS% 2 == 0):
        print("HINT:THE number is EVEN")
    elif(COUNT == 5 and NUM!= GUESS and GUESS% 2 != 0): 
        print("HINT:The number is ODD")
             
    
   
           
    NUM = int(input("Enter the number"))
        

    
    if(NUM > GUESS and 0<NUM<100):
        print("You have entered a BIGGER number")
        
    elif(NUM < GUESS  and 0<NUM<100):
        print("You have entered a SMALLER number")

        #IF A NUMBER IS OUT OF RANGE

    elif(0>NUM or  NUM>100):
        print("Out of Range: Number should be 1-100")
        break
                    
    elif(NUM == GUESS):        
        
        print("Bull`s Eye!the no is",RANDOM)        
        print("Poi Pozhappa parunga")
        break
    COUNT = COUNT+1
    while(COUNT>5):
        print("The NUMBER is",RANDOM)
        break
    
'''
     
while(COUNT ==4):
             
    if(GUESS % 2 == 0 and NUM!=GUESS):
        print("HINT:THE number is EVEN")
    elif(GUESS % 2 != 0 and NUM!=GUESS): 
        print("HINT:The number is ODD")
                
    elif(NUM == GUESS):
        print("Bull`s Eye!the no is",GUESS)        
        print("Poi Pozhappa parunga")

'''           
              
