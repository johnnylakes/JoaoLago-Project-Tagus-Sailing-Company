class Skipper():

    def __init__(self, name, lang, cat, price, type, tmax, acch, data):

        '''
        Initializes an instance of Class Skipper.
        
        Requires: 
        The name, language, category, price, type, maximum work time, accumulated work hours and the date available of the respective skipper.

        Ensures:
        An object of the class Skipper with the respective atributes name, language, category, price, type, maximum work time, accumulated work hours and the date that he is available.
        '''
         
        self._name = name
        self._lang = lang
        self._cat = cat
        self._price = price
        self._type = type
        self._tmax = tmax
        self._acch = acch
        self._data = data
        l = data.split(" ")
        self._time = l[2].replace(")","")
        self._datesch = l[1].replace("(","")
        self._timesch = l[2].replace(")","")
    
    def getName(self):

        '''
        Returns the name of the object skipper

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the name of an object of the class Skipper
        '''

        return self._name
    
    def getLang(self):
        
        '''
        Returns the language of the object skipper

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the language of an object of the class Skipper
        '''
        
        return self._lang
    
    def getCat(self):
        
        '''
        Returns the category of the object skipper

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the category of an object of the class Skipper
        '''
        
        return self._cat
    
    def getPrice(self):
        
        '''
        Returns the price of the object skipper

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the price of an object of the class Skipper
        '''
        
        return self._price
    
    def getType(self):
        
        '''
        Returns the type of the object skipper

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the type of an object of the class Skipper
        '''
        
        return self._type 
    
    def getTmax(self):
        
        '''
        Returns the maximum work time of the object skipper

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the maximum work time of an object of the class Skipper
        '''
        
        return self._tmax
    
    def getAccH(self):
        
        '''
        Returns the accumulated hours of the object skipper

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the accumulated hours of an object of the class Skipper
        '''
        
        return self._acch
    
    def getData(self):
        
        '''
        Returns the date of the object skipper

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the date of an object of the class Skipper
        '''
        
        return self._data
    
    def getTime(self):
        
        '''
        Returns the time in the 00:00 format of the object skipper

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the time in the 00:00 format of an object of the class Skipper
        '''
        
        return self._time
    
    def getDateSch(self):
        
        '''
        Returns the date of the scheduled that the skipper is related to

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the date of the schedule that the skipper is related to, of an object of the class Skipper
        '''
        
        return self._datesch
    
    def getTimeSch(self):
        
        '''     
        Returns the time of the schedule that the skipper is related to

        Requires:
        For the fucntion to be called, when it is needed

        Ensures:
        Return the time of the schedule that the skipper is related to, of an object of the class Skipper
        '''
        
        return self._timesch
    
    def setName(self, other):
        
        '''
        Update the name of the Skipper based of a given input

        Requires:
        A string representing the new name of the skipper

        Ensures:
        The update of the name for the new input
        '''
        
        self._name = other
        
    def setLang(self, other):
         
        '''
        Update the language of the Skipper based of a given input

        Requires:
        A string representing the new language of the skipper

        Ensures:
        The update of the language for the new input
        '''
        
        self._lang = other
    
    def setCat(self, other):
        
        '''
        Update the category of the Skipper based of a given input

        Requires:
        A string representing the new category of the skipper

        Ensures:
        The update of the category for the new input
        '''
        
        self._cat = other
    
    def setPrice(self, other):
        
        '''
        Update the price of the Skipper based of a given input

        Requires:
        A string representing the new price of the skipper

        Ensures:
        The update of the name for the new input
        '''
        
        self._price = other

    def setType(self, other):
        
        '''
        Update the type of the Skipper based of a given input

        Requires:
        A string representing the new type of the skipper

        Ensures:
        The update of the type for the new input
        '''
        
        self._type = other

    def setTmax(self, other):
        
        '''     
        Update the maximum work time of the Skipper based of a given input

        Requires:
        A string representing the new maximum work time of the skipper

        Ensures:
        The update of the maximum work time for the new input
        '''
        
        self._tmax = other

    def setAccH(self, other):
        
        '''
        Update the of the accumulated hours based of a given input

        Requires:
        A string representing the new accumulated hours of the skipper

        Ensures:
        The update of the accumulated hours for the new input
        '''
        
        self._accH = other

    def setData(self, other):
        
        '''
        Update the date of the Skipper based of a given input

        Requires:
        A string representing the new date of the skipper

        Ensures:
        The update of the date for the new input
        '''
        
        self._data = other

    def setTime(self, other):
        
        '''
        Update the time in the 00:00 format of the Skipper based of a given input

        Requires:
        A string representing the new time of the skipper

        Ensures:
        The update of the time for the new input
        '''
        
        self._time = other

    def setDateSch(self,other):
        
        ''' 
        Update the date of the scheduled that the skipper is related to based of a given input

        Requires:
        A string representing the new date of the scheduled that the skipper is related 

        Ensures:
        The update of the date for the new input that the skipper is related to the scheduled
        '''
        
        self._datesch = other

    def setTimeSch(self, other):
        
        '''
        Update the time of the scheduled that the skipper is related to based of a given input

        Requires:
        A string representing the new time of the scheduled that the skipper is related 

        Ensures:
        The update of the time for the new input that the skipper is related to the scheduled
        '''
        
        self._timesch = other

    def addHours(self, newHours):
        if self._accH + newHours >= self._tmax:
            self._acch = 0
        else:
            self._accH = self._accH + newHours

    def addTime(self,reqhour):
        t = self.getTime()
        t = t.replace(":","")
        s = str(int(t) + int(reqhour) * 100)
        if int(s) == 2000:
            s = str(800)
        if len(s) == 3:
            s = "0" + s[:1] + ":"  + s[1:]
        else:
            s = s[:2] + ":"  + s[2:]
        self.setTime(s)

    def __eq__(self, other):
        if type(other) == int:
            return other == 0
        else:
            return self._name == other._name
       
    def __lt__(self,other):
        return self.getName() > other.getName() 

    def __str__(self):
        return  str(self.getName()) + ", " + str(self.getLang()) + ", " + str(self.getCat()) + ", " + str(self.getPrice()) \
            + ", " + str(self.getType()) + ", " + str(self.getTmax()) + ", " + str(self.getAccH()) + ", " + str(self.getData()) 
    
    
    
    





