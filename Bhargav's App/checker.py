#Functions For Checkers
import time

def dataChecker(data): #Checks what type of data the variable is
    try:
        data = int(data)
        int == int(data)
        return True #For a number
    except:
        return False #For a string

def done(): #Asks the user if they have completed a question
    print()
    d = input('Done? ')
    print()
    d=d.upper()
    if d == 'Y':
        pass
    elif d == 'N':
        time.sleep(5)
        done()
    elif d == '':
        pass
    else:
        done()
