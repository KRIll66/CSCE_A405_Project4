class Cell:
    def __init__(self, val, index):
        self.value = val
        self.index = index
        self.domain = [1,2,3,4,5,6,7,8,9]

    def setValue(self, val):
        self.value = val
        if val != 0:
            self.domain = []

    def setDomain(self, val):
        if val in self.domain:
            self.domain.remove(val)
            
    def hasValue(self):
        if self.value != 0:
            return True
        return False

    def getValue(self):
        return self.value

    def getDomain(self):
        return self.domain

    def getIndex(self):
        return self.index