class Node:

	def __init__(self, item, nxt):
		self.mItem = item
		self.mNext = nxt
		
class Blob:

	def __init__(self):
		self.mFirst = None

	def Insert(self, item): # return false if item was a duplicate, and not inserted
		if self.Exists(item):
			return False
		n = Node(item, self.mFirst)
		self.mFirst = n
		return True
		
	def Exists(self, item):
		current = self.mFirst
		while current is not None:
			if current.mItem == item:
				return True
			else:
				current = current.mNext
		return False
	    
	def Delete(self, item): # return false if can't find item that == matches
		if not self.Exists(item):
			return False
		if self.mFirst.mItem == item:
			self.mFirst = self.mFirst.mNext
			return True
		current = self.mFirst
		while not current.mNext.mItem == item:
			current = current.mNext 
		current.mNext = current.mNext.mNext
		return True

	def Retrieve(self, item): #given item with just key field, return full item from database, return None if not.
		current = self.mFirst
		while current is not None:
			if current.mItem == item:
				return current.mItem
			else:
				current = current.mNext
		return None
		

	def Size(self):
		size = 0
		current = self.mFirst
		while current is not None:
			size += 1
			current = current.mNext
		return size

	def Traverse(self, callbackFunction): #call callback function for each item in the blob
		current = self.mFirst
		while current != None:
			callbackFunction(current.mItem)
			current = current.mNext
			
class Student:

	def __init__(self, lname, fname, ssn, email, age):

		self.lname = lname
		self.fname = fname
		self.ssn = ssn
		self.ssn_int = int(self.ssn.replace('-', ''))
		self.email = email
		self.age = age
		
	def __eq__(self, rhs):
		return self.ssn == rhs.ssn # are social security numbers equal
	
	def __ne__(self, rhs):
		return self.ssn_int != rhs.ssn_int
	
	def __lt__(self, rhs):
		return self.ssn_int < rhs.ssn_int

	def __gt__(self, rhs):
		return self.ssn_int > rhs.ssn_int

	def __le__(self, rhs):
		return self.ssn_int <= rhs.ssn_int

	def __ge__(self, rhs):
		return self.ssn_int >= rhs.ssn_int
		
	def __int__(self):
		return int(self.ssn.replace('-', ''))

	def getLName(self):
		return self.lname

	def getFName(self):
		return self.fname

	def getSSN(self):	
		return self.ssn

	def getEmail(self):
		return self.email

	def getAge(self):
		return self.age