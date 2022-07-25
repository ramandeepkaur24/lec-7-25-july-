#private

class Base:
	def __init__(self):
		self.a = "GeeksforGeeks\n"
		self.__c = "GeeksforGeeks"
		print(self.a,self.__c)
class Derived(Base):
    def __init__(self):
        print("Calling private member of base class: ")
        super().__init__()
obj = Derived()

