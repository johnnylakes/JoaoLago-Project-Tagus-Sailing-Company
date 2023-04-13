class Request():

    def __init__(self,name,lang,cat,type,numbh):
        self._name = name
        self._lang = lang
        self._cat = cat
        self._type = type
        self._numbh = numbh
    
    def getName(self):
        return self._name
    
    def getLang(self):
        return self._lang
    
    def getCat(self):
        return self._cat
    
    def getType(self):
        return self._type
    
    def getNumbH(self):
        return self._numbh

    def setName(self, other):
        self._name = other
    
    def setLang(self, other):
        self._lang = other

    def setCat(self, other):
        self._cat = other

    def setType(self, other):
        self._type = other

    def setNumbH(self, other):
        self._numbh = other

    def __eq__(self,other):
        return self._name == other.name
    
    def __lt__(self,other):
        return self._numbh < other._numbh

    def __str__(self):
        return "(" + self.getName() + ", " + self.getLang() + ", " + self.getCat() + ", " + self.getType() + ", " + self.getNumbH() + ")"
    