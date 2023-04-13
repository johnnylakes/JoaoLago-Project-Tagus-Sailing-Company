def isIntersect(lang1,lang2):
    '''
        Checks if a list has a common element with another list.

        Requires:
        Two lists that need to be compared.

        Ensures:
        Return true if there is a common element within the two lists.
    '''

    list1 = lang1.replace('(', '').replace(")", '').replace(" ","").split(";")
    list2 = lang2.replace('(', '').replace(")", '').replace(" ","").split(";")
    return set(list1).intersection(set(list2)) != set([])
           
def checkEquals(att1,att2):
    '''
        Checks if two atributes of objects are equal.

        Requires:
        Two atributes that need to be compared.

        Ensures:
        Return true if they are equals.
    '''

    at1 = att1.replace(" ","")
    at2 = att2.replace(" ","")
    return at1 == at2

def checkObjectIsEmpty(object):
    '''
        Checks if a variable is an object or zero.

        Requires:
        An object as an argument.

        Ensures:
        Return true the value of the variable is zero.
    '''
       
    value = object
    if value == 0:
        return True
    else:
        return False
    
def hourToInt(time):
    """
    Reads a string representing a given time and returns a integer representing 
    the portion of the time corresponding to the hour.

    Requires:
    A group of numbers in the time representing format (XX:XX) as a string

    Ensures:
    An integer representing the hourly portion corresponding to a given time.
    """
    t = time.split(":")
    return int(t[0])

def minutesToInt(time):
    """
    Reads a string representing a given time and returns a integer representing 
    the portion corresponding to the minutes part of the time.

    Requires:
    A group of numbers in the time representing format (XX:XX) as a string 
    and a value representing the minutes lesser than 60

    Ensures:
    An integer representing the minutes portion corresponding to a given time.
    """
    t = time.split(":")
    return int(t[1])
    
def intToTime(hour, minutes):
    """
    Receives two intergers representing the hour and the minutes of a 
    given time and returns the corresponding time of the two intergers as a string.

    Requires:
    Two intergers representing the hour and the minutes of a given time, 
    the hours cannot exced 24 and the minutes cannot exced 60.

    Ensures:
    A string representing the hour and the minutes of a given time
    by concatenating the intergers hours and minutes.
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m

def dayToInt(date):
    """
    Reads a string representing a given date and returns a integer representing 
    the portion corresponding to the day part of the date.

    Requires:
    A group of numbers in the date representing format (XX/XX/XX) as a string 
    and a value representing the days 

    Ensures:
    An integer representing the day portion corresponding to a given date.
    """
     
    day = date.split(':')[0]
    return int(day)

def monthToInt(date):
    """
    Reads a string representing a given date and returns a integer representing 
    the portion corresponding to the month part of the date.

    Requires:
    A group of numbers in the date representing format (XX/XX/XX) as a string 
    and a value representing the month

    Ensures:
    An integer representing the day portion corresponding to a given date.
    """
    month = date.split(':')[1]
    return int(month)

def yearToInt(date):
    """
    Reads a string representing a given date and returns a integer representing 
    the portion corresponding to the year part of the date.

    Requires:
    A group of numbers in the date representing format (XX/XX/XX) as a string 
    and a value representing the year 

    Ensures:
    An integer representing the year portion corresponding to a given date.
    """
    year = date.split(':')[2]
    return int(year)

def intToDate(day,month,year):
    """
    Receives three intergers representing the day, month and the year of a 
    given time and returns the corresponding date of the three intergers as a string.

    Requires:
    Three intergers representing the day, month and the year of a given date.

    Ensures:
    A string representing the day, month and the year of a given date
    by concatenating the intergers day, month and year.
    """

    d = str(day)
    m = str(month)
    y = str(year)
    if day < 10:
        d = "0" + d
    elif month < 10:
        m = "0" + m
    return d + ":" + m + ":" + y

def UpdateFileTime(date,time):
    '''
        Updates the time of file name from a given date and time.

        Requires:
        Two string arguents, date and time.

        Ensures:
        Returns a list of two values representing the updated time and date.
    '''

    day = dayToInt(date)
    month = monthToInt(date)
    year = yearToInt(date)
    minutes = minutesToInt(time) + 30
    hour = hourToInt(time)
    if minutes == 60:
        minutes = 0
        hour += 1
    else:
        if hour > 20:
            hour = 8
            day += 1

        elif hour == 20 and minutes == 30:
            hour = 8
            day += 1
        
        else:
            if day > 30:
                day = 1
                month += 1
            else:
                if month > 12:
                    month = 1
                    year += 1            
    Newtime = intToTime(hour,minutes)
    NewDate = intToDate(day,month,year)
    return [NewDate,Newtime]

def createFileName(filename,time):
    '''
        Creates a filename from a previous filename and a given time.

        Requires:
        A string representing a filename and a time string.

        Ensures:
        Return a string representing an updated filename.
    '''
     
    minutes = minutesToInt(time) + 30
    hour = hourToInt(time)
    if minutes == 60:
        minutes = 0
        hour += 1
    else:
        if hour > 20:
            hour = 8

        elif hour == 20 and minutes == 30:
            hour = 8
    if "skippers" in filename:
       
        return f"skippers{hour}h{minutes}.txt"
    else:
        
        return f"schedule{hour}h{minutes}.txt"

def createHeader(filename,day,time):
    '''
        Creates a header depending on the name of the file, the day and the time given as arguments.

        Requires:
        Three strings representing the filename, day and time.

        Ensures:
        Return a list with elements needed to produce a header in the text file.
    '''

    if "skipper".casefold() in filename.casefold():
        header = ["Company:","Tagus Sailing","Day:",day,"Time:",time,"Skippers:"]
    else:
        header = ["Company:","Tagus Sailing","Day:",day,"Time:",time,"Schedule:"]
    return header

def checkIfSchStay(filename):
    '''
        Checks what lines in a given text file should stay in the file and what should leave.

        Requires:
        Filename representing a text file.

        Ensures:
        Return a list with all lines that should stay in the file.
    '''

    inFile = open(filename,"r")
    fileList = inFile.readlines()
    day = fileList[3]
    time = fileList[5]
    intTime = time.replace(":","")
    schDay = dayToInt(day)
    schMonth = monthToInt(day)
    schYear = yearToInt(day)
    oldSch = fileList[7:]
    copyoldSch = []
    for z in oldSch:
        oldSchTime = z[12:17].replace(":","")
        matchNumbH = z[19]
        matchDay = dayToInt(z[0:10])
        matchMonth = monthToInt(z[0:10])
        matchYear = yearToInt(z[0:10])
        if matchYear > schYear:
            copyoldSch.append(z)
        else:
            if matchMonth > schMonth:
                copyoldSch.append(z)
            else:
                if matchDay > schDay:
                    copyoldSch.append(z)
                else:
                    if int(oldSchTime) + int(matchNumbH)*100  > int(intTime):
                        copyoldSch.append(z)
    for p in range(len(copyoldSch)):
        copyoldSch[p] = copyoldSch[p].replace("\n","")
    return copyoldSch, day 



def sortList(list, date):
    '''
        Sorts a given list based on three criteria: if there is an Not-asigned, the time, the day.

        Requires:
        A list and a date.

        Ensures:
        Return a sorted list .
    '''
       
    x = []
    y = []
    z = []
    for i in list:
        new = i.split(",")
        if " Not-asigned " in new[1]:
            x.append(i)
        elif str(new[0]) == str(date):
            y.append(i)
        else:
            z.append(i)
    newY = []
    for i in y:
        new = i.split(",")
        try:
            new[1] = int(new[1].replace(":", ""))
        except ValueError:
            new[1] = int(new[1].getTime().replace(":", ""))
        newY.append(new)
    newY.sort(key = lambda newY: (newY[1],newY[3]))
    listY = []
    for i in newY:  
        i[1] = str(i[1])
        if len(i[1]) == 3:
            v = "0" + i[1][:1] + ":"  + i[1][1:]
        else:
            v = i[1][:2] + ":"  + i[1][2:]
        i[1] = v
        listY.append(", ".join(i))   
    newZ = []
    for i in z:
        new = i.split(",")
        new[1] = int(new[1].replace(":", ""))
        newZ.append(new)
    newZ.sort(key = lambda newZ: (newZ[1],newZ[3]))
    listZ = []
    for i in newZ:
        i[1] = str(i[1])
        if len(i[1]) == 3:
            p = "0" + i[1][:1] + ":"  + i[1][1:]
        else:
            p = i[1][:2] + ":"  + i[1][2:]
        i[1] = p
        listZ.append(", ".join(i))
    return x + listY + listZ



def checkFileError(filename):
    '''
        Checks if the time of a given file is the same as the time in the file name.

        Requires:
        A file name in the XXXXh.txt format, either skipper or schedule.

        Ensures:
        A file name in the XXXXh.txt format corrected if the time in the file was diferent than the file name.
    '''
    fileNameString = filename
    infile = open(filename, 'r')
    fileList = infile.readlines()
    fileHour = fileList[5].replace("\n","")
    fileNameHour = fileNameString[29:34].replace("h",":")
    if fileHour != fileNameHour:
        fileHour = fileNameHour
    return fileHour






checkFileError("testSets_v1/testSet4/skippers13h00.txt")






a = ['10:11:2022, 19:00, 1, Afonso Amaro, 50, Hans Mathiesen', '11:11:2022, 08:00, 4, Carla Teixeira, 200, Charles Bronson', '10:11:2020, Not-asigned , Mario Scorcese', '10:11:2020, Not-asigned , Stanislav Osenov', '10:11:2022, 18:00,  1, Diogo Domingues, 120, Pierre Martin', '11:11:2022, 04:00,  4, Afonso Amaro, 200, Paco Moreno']
            


#sortList(a,t)

#intToDate(1,9,2022)

#print(dayToInt("12:09:2022"))

#print(createFileName("kippers17h00.txt","17:00"))

#checkIfSchStay("projeto/testSets_v1/testSet1/schedule17h00.txt")






            
            








#req1 = request("Vladislav Maraev", "(russian; english)"," 2*", "price", "8")

#skip1 = Skipper("Afonso Amaro",  "(english; french; portuguese; spanish)","  2*",  "50",  "price",  "50",  "35",  "(10:11:2022 12:00)")

#skip2 = Skipper("Carla Teixeira", "(english; spanish; portuguese)", "2*", "50", "price", "20", "20", "(11:11:2022, 12:00)")

#skip4 = Skipper("Teixeira", "(english; spanish; portuguese)", "2*", "50", "price", "20", "20", "(11:11:2022, 12:00)")

#skip3 = Skipper("Diogo Domingues", "(french; portuguese)", "3*", "120", "comfort", "40", "24", "(10:11:2022, 18:00)")

#req2 = request("John Rosner", "(english)", "1*", "comfort", "2")

#req3 = request("François Macron", "(french; german)", "1*", "price", "2")

#l1 = [req1,req2,req3]
#l2 = [skip1,skip2,skip3,skip4]

#for r in l1:
#    print(findMatchingSkipper(r,l2))
   
        

#print(skip1.getcat())
#print(req1.getCat())

#print(checkEquals(skip1.getcat(),req1.getCat()))
#print(checkEquals(skip1.gettype(),req1.getType()))
#print(isSubset(skip1.getlang(),req1.getLang()))
#dateUpdate(skip1,8)