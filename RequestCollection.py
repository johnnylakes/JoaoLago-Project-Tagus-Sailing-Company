from Request import Request

class RequestCollection():

    def __init__(self):
        self._collection = []
        self._filedate = ""

    def getreqCollection(self):
        return self._collection

    def getFileDate(self):
        return self._filedate
    
    def setreqCollection(self, other):
        self._collection = other

    def setFiledate(self,other):
        self._filedate = other
    
    def resetCollection(self):
        self._collection = []

    def createCollection(self,filename):
        file = open(filename, "r")
        file_List = file.readlines()
        self.setFiledate(file_List[3].replace("\n",""))
        for line in file_List:
            if file_List.index(line) > 6:
                reqData = line.rstrip().split(",")
                self._collection.append(Request(reqData[0], reqData[1],reqData[2], reqData[3],reqData[4]))

    def __str__(self):
        stringList = ""
        for i in self._collection:
            stringList +=(i.__str__()) + "\n"
        return stringList
