from Skipper import Skipper

class SkipperCollection():

    def __init__(self):
        self._collection = []

    def getCollection(self):
        return self._collection

    def setcollection(self, other):
        self._collection = other

    def resetCollection(self):
        self._collection = []

    def createCollection(self,filename):
        file = open(filename, "r")
        file_List = file.readlines()
        for line in file_List:
            if file_List.index(line) > 6:
                skipData = line.rstrip().split(",")
                self._collection.append(Skipper(skipData[0], skipData[1],skipData[2], skipData[3],skipData[4],skipData[5],skipData[6],skipData[7] + skipData[8]))

    def writefile(self,date,time):
        timecopy = time
        timecopy = timecopy.replace(":","h")
        file = open(f"skipper{timecopy}.txt","w")
        header = ["Company:","Tagus Sailing","Day:",date,"Time:",time,"Skippers:"]
        for i in header:
            file.writelines(i + "\n")
        for i in self._collection:
            file.writelines(i.__str__() + "\n")
        return file

    def updateNewSkippersCollection(self,newCollection):
        for i in newCollection:
            self._collection.append(i)
      
    def __str__(self):
        stringList = ""
        for i in self._collection:
            stringList += (i.__str__()) + " "
        return stringList
        
    
                
             
        
             
        



            
    




#col = skipperCollection()

#col.createCollection("projeto/testSets_v1/testSet1/skippers17h00.txt")

#col2 = skipperCollection()
#col2.createCollection("projeto/testSets_v1/testSet2/skippers18h00.txt")

#col3 = skipperCollection()
#col3.createCollection("projeto/testSets_v1/testSet3/skippers10h00.txt")

#col4 = skipperCollection()
#col4.createCollection("projeto/testSets_v1/testSet4/skippers13h00.txt")


#print(col)

        
   


