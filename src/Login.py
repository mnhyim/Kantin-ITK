class Login:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.status = ""
        self.role = ""
        
    def getUser(self):
        return self.username

    def getPass(self):
        return self.password
    
    def setUserPass(self, x):
        self.username = x
    
    def setPass(self, x):
        self.password = x        

    def setStatus(self,x):
        self.status = x

    def getStatus(self):
        return self.status

    def setRole(self,x):
        self.role = x

    def getRole(self):
        return self.role

    
