import math

class Blob:
	
	def __init__(self, datasize):
		tablesize = datasize*2+1
		while not self.is_prime(tablesize):
			tablesize += 2
		self.m_table = [None] * tablesize
		# self.m_table = []
		# for num in range(tablesize):
		    # self.m_table.append(None)
		self.m_size = 0 # add 1 for successful insert, minus 1 for delete
	
			
	
	def is_prime(self, x):
		s = int(math.sqrt(x))
		for i in range(2, s+1):
			if x % i == 0:
				return False
			return True
			


	def Traverse(self, callback):
		for item in self.m_table:
			if item:
				callback(item)
				
				
	def Size(self):
		count = 0
		for item in self.m_table:
			if item:
				count += 1
		return count
		
		
	def Exists(self, item):
		key = int(item)
		index = key % len(self.m_table)
		while True:
			if self.m_table[index] is None:
			    return False
			if self.m_table[index] and self.m_table[index] == item:
				return True
			else:
				index += 1
				if index >= len(self.m_table):
					index = 0
					

	def Insert(self, item):
		if self.Exists(item):
			return False
		key = int(item)
		index = key % len(self.m_table)
		while self.m_table[index]:
			index += 1
			if index >= len(self.m_table):
				index = 0
		self.m_table[index] = item
		self.m_size += 1
		return True	
			
		
	def Delete(self, item):
		if not self.Exists(item):
			return False
		key = int(item)
		index = key % len(self.m_table)
		while not (self.m_table[index] and self.m_table[index] == item):
			index += 1
			if index >= len(self.m_table):
			    index = 0
		self.m_table[index] = False
		return True
		
	
	def Retrieve(self, item):
		if not self.Exists(item):
			return None
		key = int(item)
		index = key % len(self.m_table)
		while not (self.m_table[index] and self.m_table[index] == item):
			index += 1
			if index >= len(self.m_table):
			    index = 0
		# self.m_table[index] = item
		return self.m_table[index]
		
		
class Student:

	def __init__(self, lname, fname, ssn, email, age):

		self.lname = lname
		self.fname = fname
		self.ssn = ssn
		self.email = email
		self.age = age
		
	def __eq__(self, rhs):
		return self.ssn == rhs.ssn # are social security numbers equal
	
	def __ne__(self, rhs):
		return self.ssn != rhs.ssn
		
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