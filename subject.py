class Subject: 
    def __init__(self,name,heldLecture,attendedLecture):
        self.heldLecture = heldLecture
        self.attendedLecture = attendedLecture
        self.currAttendance = attendedLecture/heldLecture
        self.name = name
    
    def getCurrentAttendance(self): 
        currAttendance = ((self.attendedLecture)/(self.heldLecture)) * 100
        return currAttendance
    
    def getHeldLecture(self): 
        return self.heldLecture
    
    def getAttendedLecture(self): 
        return self.attendedLecture
    
    def getName(self): 
        return self.name
    
    
    


