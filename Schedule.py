from auxy import *
from Request import *
from Skipper import *
from SkipperCollection import *
from RequestCollection import *

class Schedule():

    def __init__(self):
        '''
        Initializes an instance of Class Schedule.
        
        Requires: 
        An instance of the class schedule to be created 

        Ensures:
        An object of the class Schedule with the respective atributes match, time, schedule date, schedule time
        '''
        self._match = []
        self._time = ""
        self._schDate = ""
        self._schTime = ""

    def getTime(self):
        '''
        Returns the time of the object of the class Schedule

        Requires:
        For the function to be called, when it is needed

        Ensures:
        Return the time of an object of the class Schedule
        '''
        return self._time
    
    def getSchDate(self):
        '''
        Returns the schedule date atribute of an object of the class Schedule

        Requires:
        For the function to be called, when it is needed

        Ensures:
        Return the  schedule date of an object of the class Schedule
        '''
        return self._schDate
    
    def getSchTime(self):
        '''
        Returns the schedule time of an object of the class schedule

        Requires:
        For the function to be called, when it is needed

        Ensures:
        Return the schedule time of an object of the class Rquest
        '''
        return self._schTime
    
    def getCollection(self):
        '''
        Returns the colection of the scheedule object of the class schedule

        Requires:
        For the function to be called, when it is needed

        Ensures:
        Return the colection of an object of the class schedule
        '''
         
        return self._match
    
    def setSchDate(self,other):
        '''
        Update the schedule date of the object based of a given input

        Requires:
        A string representing the new schedule date of the schedule

        Ensures:
        The Update of the schedule date for the new input
        '''
        self._schDate = other

    def setSchTime(self,other):
        '''
        Update the schedule time of the objet request based of a given input

        Requires:
        A string representing the new category of the schedule

        Ensures:
        The Update of the schedule time for the new input
        '''

        self._schTime = other

    def setTime(self,other):
        '''
        Update the time of the object schedule based of a given input

        Requires:
        A string representing the new time of the schedule

        Ensures:
        The Update of the time for the new input
        '''
        self._time = other

    def displayCol(self):
        '''
        Return the data of the class converted to the text format 
            
        Requires: 
        The method to be called when needed

        Ensures:
        A concateneted string of the returned values of the method __str__() of the skipper object and the request object in the match atribute.
        '''
        for i in self._match:
            print(i[0].__str__(),i[1].__str__())
            
    def matchCol(self,skipcol,reqcol):
        '''
        Match skipers objects with the corresponding requests 
        objects from a colection of skippers objects and from a colection of requests objects and updates de atribute match
            
        Requires:
        A request object colection and a skipper object colection. 

        Ensures:
        The match atribute is updated with the corresponding skipper/request match.
        '''
        self._match = []
        self.setTime(reqcol.getFileDate())
        for req in reqcol.getreqCollection():
            sk_escolhido = self.findMatchingSkipper(req,skipcol.getCollection())
            self._match.append((req,sk_escolhido)) 
        reqcol.resetCollection()

    def findMatchingSkipper(self,req,skipcol):
        '''
        Match skipers objects with the corresponding requests objects 
            
        Requires:
        A request object and a skipper colection object. 

        Ensures:
        A skipper object that matchs the requirements of the requeste object.
        '''
        possibleMatch = []
        for skip in skipcol:
            date_hour = skip.getData()
            dateList = date_hour.replace("(","").replace(")","").split(' ')
            if isIntersect(req.getLang(),skip.getLang())\
                and checkEquals(req.getCat(),skip.getCat())\
                    and checkEquals(req.getType(),skip.getType()) \
                        and int(skip.getAccH()) + int(req.getNumbH()) <= int(skip.getTmax())\
                            and int(req.getNumbH()) + hourToInt(dateList[1]) <= 20:
                possibleMatch.append(skip)
        sk_escolhido = self.tieBreaker(possibleMatch)
        if type(sk_escolhido) != str:
            sk_escolhido.setAccH(int(sk_escolhido.getAccH()) + int(req.getNumbH()))
            self.dateUpdate(sk_escolhido,req.getNumbH())     
        return sk_escolhido
    
    def dateUpdate(self,skipper,reqhour):
        '''
        Updates the skiper objects time taking into acount the number of hours in the corresponding requests objects 
                
        Requires:
        A request object and a skipper object. 

        Ensures:
        That the time of a especific skipper is updated based on the request object number of hours.
        '''
        reqhour = int(reqhour)
        date_hour = skipper.getData()
        date_hour = date_hour[1:]
        dateList = date_hour.replace("(","").replace(")","").split(' ')
        minutes = minutesToInt(dateList[1])
        hour = hourToInt(dateList[1])
        date = dateList[0]
        day = dayToInt(date)
        month = monthToInt(date)
        year = yearToInt(date)
        if minutes == 0:
            if hour + reqhour <= 20:
                hour+=reqhour   
            else:
                hour = 8 + reqhour
                if day < 30:
                    day+=1
                else:
                    day = 1
                    if month < 12:
                        month += 1
                    else:
                        month = 1
                        year += 1
        else:
            if hour + reqhour < 19:
                hour += reqhour
            else:
                hour = 8
                if day < 30:
                    day+=1
                else:
                    day = 1
                    if month < 12:
                        month += 1
                    else:
                        month = 1
                        year += 1
        timeToString = intToTime(hour,minutes)
        dateToString = intToDate(day,month,year)
        skipper.setData("(" + dateToString + " " + timeToString + ")")
      
    def dataUpdateSch(self,skipper,reqhour):
        '''
        Updates the skipper objects time inside the schedule taking into acount the number of hours in the corresponding requests objects 
                
        Requires:
        A request object and a skipper object. 

        Ensures:
        That the time of a especific skipper is updated based on the request object number of hours.
        '''
          
        req= int(reqhour)
        date = skipper.getDateSch()
        time = skipper.getTimeSch()
        hour = hourToInt(time)
        minutes = minutesToInt(time)
        time = time.replace(":","")
        time = int(time)
        day = dayToInt(date)
        month = monthToInt(date)
        year = yearToInt(date)
        if time + (req * 100) >= 2000:
            hour = 8
            minutes = 0
            day+=1
        else:
            hour = hour + req
        skipper.setDateSch(intToDate(day,month,year))
        skipper.setTimeSch(intToTime(hour,minutes))
        

    def tieBreaker(self,PM):
        '''
       Analises a list of possible skippers and returns the best sutable skipper for a especific request 
            
        Requires:
        A list of skippers matchig a request 

        Ensures:
        A skipper object that matchs the requirements of the requeste object and is better suited than the other skippers.
        '''
         
        if len(PM) == 0:
            return "Not-assigned"
        for i in range(len(PM)):
            if len(PM) == 1:
                return PM[0]
            for j in range(i+1,len(PM)):
                sk_escolhido = PM[i]
                if sk_escolhido.getPrice() > PM[j].getPrice():
                    sk_escolhido = PM[j]
                elif sk_escolhido.getPrice() == PM[j].getPrice():
                    if int(sk_escolhido.getAccH()) > int(PM[j].getAccH()):
                        sk_escolhido = PM[j]
                    elif sk_escolhido.getAccH() == PM[j].getAccH():
                        if sk_escolhido.getName() > PM[j].getName():
                            sk_escolhido = PM[j]
        return sk_escolhido
                
    def __str__(self):
        '''
        Return the data of the class converted to the text format 
            
        Requires: 
        The method to be called when needed

        Ensures:
        A concateneted string of the returned values of the method __str__() of the skipper object and the request object in the match atribute.
        '''
           
        stringList = []
        for i in self._match:
            if type(i[1]) == str:
                stringList.append(f"{self.getTime()}, Not-asigned , {i[0].getName()}")
            else:
                if i[1].getTimeSch() == "20:00":
                    self.dataUpdateSch(i[1],i[0].getNumbH())
                stringList.append(f"{i[1].getDateSch()},{i[1].getTimeSch()},{i[0].getNumbH()},{i[1].getName()},{str(int(i[1].getPrice()) * int(i[0].getNumbH()))},{i[0].getName()}")
                self.dataUpdateSch(i[1],i[0].getNumbH())
                i[1].addTime(i[0].getNumbH())
        return stringList

    
