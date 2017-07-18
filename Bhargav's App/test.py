#Test environment
#Make a counte
from checker import *

wrong = []
correct = []
saved =[]
ans =''
def right(scales,x):#When attaching to main code this should recieve the scale and its position
    global ans
    print('can you play', scales[x])
    canYou()
    ans=ans.upper()
    goit(ans,x,scales)
    sort()

def canYou():#Asks the user weather or not they got the answer correct or not
    global ans
    ans = input('Enter Y if you got it correct N otherwise ')
    ans = ans.upper()
    dataChecker(ans)
    if dataChecker == True:
        canYou()
    elif ans == '':
        canYou()
    elif ans == 'Y' or ans == 'N':
        pass
    else:
        canYou()
           
def goit(t,x,scales):#Takes in the user input, scale position and scale respectively. Appends to the respective list
    if t == 'Y':
        print('Well done')
        correct.append(scales[x])
        
    elif t == 'N':
        print('Oh noes')
        wrong.append(scales[x])

def sort(): #To replace the how many scales you got right so there aren't any duplicates
    for i in wrong:
        if i not in saved:
            saved.append(i)
    for i in correct:
        if i in saved:
            saved.remove(i)


#The Below Is Not Implemented
            
def counted(x): 
    if len(x) == 0:
        print('Well done, you know all of them')
    elif len(x) == 1:
        print('This is the scale you do not know how to play',x)
    elif len(x) > 1:
        print('These are the scales you do not know how to play', saved)

def countDown(x,y):#x is the iterations, y is the iterations completed
    u = x - y
