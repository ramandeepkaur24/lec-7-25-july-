class Demo:
    def __init__(self,name,address):
        self.__name=name
        self.__address=address
    def setname(self,name,address):
        self.__name=name
        self.__address=address
    def getname(self):
        return self.__name,self.__address
ob=Demo("Raman","shimlapuri")
ob.setname("Raman","shimlapuri")
print(ob.getname())
