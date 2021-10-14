n=18
print("Enter number of guesses")
guess= int(input())
print("Enter number")

i=0
while (guess >=0):
    guess= guess-1
    i=i+1
    number= int(input())
    if (guess==0):
        print("Chances over!!")
        break
    if (number< n):
        print("Less than  number!! Only ",guess ,"guesses remaining")
        
    elif (number >n):
        print("Greater than  number!! Only ",guess ,"guesses remaining")
        
    elif (number== n):
        print("Congractulations!! ")
        print("Number of guesses you took:" , i)
        break 
    
    else:
        print("something weent wrong")
    
