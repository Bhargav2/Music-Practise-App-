#Charlie version of Practise Scales App
from random import randint
import time
from checker import*
from test import*
from filex import*

majors = ['Bb major', 'Bb major arpeggio' ,'A major', 'A major arpeggio', 'E major', 'E major arpeggio', 'C major', 'C major arpeggio', 'Eb major', 'Eb major arpeggio', 'G major', 'G major arpeggio', 'Ab major', 'Ab major arpeggio']
minors = ['B minor harmoic', 'B minor arpeggio', 'C# minor harmonic', 'C# minor arpeggio', 'F minor harmonic', 'F minor arpeggio', 'C minor harmonic', 'C minor arpeggio', 'A minor harmonic', 'A minor arpeggio', 'F# minor harmonic', 'F# minor arpeggio']
chromatic = ['Chromatic scale starting on Eb', 'Chromatic scale starting on E']
dominant = ['Diminished seventh starting on E','Dominant seventh in the key of C','Dominant seventh in the key of F', 'Dominant seventh in the key of Bb']
scale = ''
iterations = 0
previous = False

def start():
    global previousResult
    global previous
    t = callback()
    previousResult = t #Temporary Store as the list is required for the scalesToRevise session
    t = len(t) #Essentially gets the numerical value for the amount of lines
    print(t)
    if t > 0: #If there are more than one items then the file is erased
        previous = True
        delContents()
    question0()
        
def question0():
    print('This app is made for flute.')
    grade = input('What grade are you doing? Input a number ')
    d = dataChecker(grade)
    d = int(d)
    if d == False:
        question0()
    elif d == True:
        if grade == 0 and (grade > 8 or grade < 0):
            print('Grades go up from 1 to 8')
            question0()
        else:
            print('You are doing grade',grade)
            if grade == 1:
                grade = grade1
            #from grades import grade
    question01()
    
def question01():
    if previous == True:
        q = input('Would you like to practise scales that you got wrong?')
        print()
        d = dataChecker(q)
        q=q.upper()
        if d == True:
            question01()
        else:
            if q == 'Y':
                scalesToRevise()
            else:
                question1()
    else:
        question1()

def scalesToRevise():#New
    print('This is for practising scales that you got wrong last time')
    for i in range (len(previousResult)):
        print('Play', previousResult[i])
        right(previousResult,i)
        done()
    print('These are the scales that you do not know how to play ',saved)
    callin(saved)
    question4()
    
def question1():
    global q
    q = input('Would you like to do a overall Practise Session [Y/N]: ')
    print()
    d = dataChecker(q)
    q=q.upper()
    if d == True:
        print('You need to enter a string')
        print()
        question1()
    else:
        question11()

def question11():
    global q
    if q == 'N':
        t = input('Would you like to practise a whole scale type? ')
        t =t.upper()
        if t == 'Y':
            allScale()
        elif t == 'N':
            print()
            print('You can choose to  select the amount of a scale type of your choice you would like to practise')
            print()
            question2()
        else:
            question11()
    elif q == 'Y':
        practiseSession()
    else:
        question1()

def question2():
    global scale
    print()
    scale = input('Enter M for majors, Mi for Minors, C for Chromatic, D for dominant ')
    print()
    d = dataChecker(scale)
    scale = scale.upper()
    if d == True:
        question2()
    elif scale == 'M' or scale == 'MI' or scale == 'C' or scale == 'D':
        question3()
        return True
    else:
        question2()

def question3():
    global iterations
    iterations = input('Enter the amount of scales you want to practise ')
    print()
    d = dataChecker(iterations)

    if d == False:
        question3()
    elif d == True and (int(iterations) < 0 or int(iterations) == 0):
        print('You need to enter a positive number')
        print()
        question3()

    else:
        main()

def question4():
    print()
    repeat = input('Would you like to have another session ')
    print()
    repeat = repeat.upper()
    if repeat == 'Y':
        question01()
    elif repeat == 'N':
        print('Bye, may the tune be with you, may the tune be with you always.')
    else:
        print('You need to enter Y/N')
        question4()

def random(x,y):
    v=0
    for i in range(y):
        v=v+1
        f = y
        f = f - v
        t = randint(0,len(x)-1)
        print('play',x[t])
        time.sleep(5)
        right(x,t)#x is the scale and t is the random selection
        if y > 1:
            print('There are',f,'scales remaining')
        elif y == 1:
            print(f,'scale remaining')
        else:
            print('Session Complete')
        done()
    print('These are the scales you do not know how to play',saved)
    callin(saved)
    question4()

def practiseSession():
    global iterations
    iterations = input('Enter how may scales you want to practise ')
    print()
    d = dataChecker(iterations)
    if d == False:
        practiseSession()
    elif d == True and (int(iterations) < 0 or int(iterations) == 0):
        print('You need to enter a positive number')
        print()
        practiseSession()
    else:
        practiseSession2()
        

def practiseSession2():
    global scaleSelection
    global iterations
    iterations = int(iterations)
    v=0
    for i in range(iterations):
        v=v+1
        x = randint(1,4)
        if x == 1:
            scaleSelection = majors
        elif x == 2:
            scaleSelection = minors
        elif x == 3:
            scaleSelection = chromatic
        else:
            scaleSelection = dominant
            
        y = iterations
        y = y - v

        t = randint(0,len(scaleSelection)-1)
        print('Play', scaleSelection[t])
        print()
        time.sleep(5)
        right(scaleSelection,t)
        if y > 1:
            print('There are',y,'scales remaining')
        elif y == 1:
            print(y,'scale remaining')
        else:
            print('Session Complete')
        done()
    print('These are the scales you do not know how to play',saved)
    callin(saved)
    question4()
    
def main():
    global iterations
    global scale
    iterations = int(iterations)
    if scale == 'M':
        scaleSelection = majors
    elif scale == 'Mi':
        scaleSelection = minors
    elif scale == 'C':
        scaleSelection = chromatic
    else:
        scaleSelection = dominant
    random(scaleSelection,iterations)
    
def allScale():
    global scale
    scale = input('Enter M for majors, Mi for Minors, C for Chromatic, D for dominant ')
    print()
    scale = scale.upper()
    d = dataChecker(scale)
    if d == True:
        allScale()
    elif d == False:
        if scale == 'M':
            scaleSelection = majors
        elif scale == 'MI':
            scaleSelection = minors
        elif scale == 'C':
            scaleSelection = chromatic
        elif scale == 'D':
            scaleSelection = dominant
        else:
            allScale() 
    x = 0
    for i in range(len(scaleSelection)):
        x = x + 1
        time.sleep(1)
        print()
        print('Play',scaleSelection[x-1])
        right(scaleSelection,(x-1))
        done()
        y = len(scaleSelection)# All of the count down code is to be replaced
        y = y - x
        if y > 1:
            print('There are',y,'scales remaining')
        elif y == 1:
            print(y,'scale remaining')
        else:
            print('Session Complete')#
    print('These are the scales you do not know how to play',saved)#to be replaved with a function
    callin(saved)
    question4()
    
start()
       

