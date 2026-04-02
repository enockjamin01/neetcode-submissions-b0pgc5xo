class MinStack:

    def __init__(self):
        self.st=[]
        self.ms=[]

    def push(self, val: int) -> None:
        if not self.ms:
            self.ms.append(val)
        else:
            if self.ms[-1] >= val:
                self.ms.append(val)
        self.st.append(val)
        

    def pop(self) -> None:
        if self.ms:
            if self.ms[-1]==self.st[-1]:
                self.ms.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        if self.ms:
            return self.ms[-1]
        
