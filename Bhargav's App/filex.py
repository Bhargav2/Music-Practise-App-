#Code for saving data to a file


def callin(lists): #Saves the list in to the txt file
    file = open("sample.txt","w")
    for element in lists:
        file.write(element+"\n")
    file.close()
    #callback()

def callback():
    global List
    List = [] #Empty list to find the lenth later
    file = open("sample.txt","r")
    lines = file.readlines() #Lines in txt file are saved 
    file.close()
    for line in lines:
        a = line.strip("\n")#Removes all the white space so that each line can be counted as one.
        List.append(a)#Applies all the lines in to the list
    return List
    

def delContents():#Essentially wipes the file clean
    file = open("sample.txt","w")
    file.seek(0)
    file.truncate()
    file.close()
   
    
    


