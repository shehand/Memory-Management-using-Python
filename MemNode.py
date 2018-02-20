class MemNode:
    def __init__(self):
        
        self.startAddress = None
        self.endAddress = None
        self.processID = None
        self.hole = True
        self.next = None

    def freeMem(self):
        self.processID = None
        self.hole = True

    def setProcess(self, pID):
        self.processID = pID
        self.hole = False

    def setSize(self, startAddress, endAddress):
        self.startAddress = startAddress
        self.endAddress = endAddress

    def printSize(self):
        return self.endAddress - self.startAddress
