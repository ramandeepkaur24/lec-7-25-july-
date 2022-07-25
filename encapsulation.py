#protected

class Base:
	def __init__(self):
		self._a = 2
		print("this is in base class",self._a)
class Derived(Base):
	def __init__(self):
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)
obj1=Derived()
obj2=Base()
