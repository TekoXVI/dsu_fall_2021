class Node:
    
    def __init__(self, item):
        self.mItem = item
        self.mL = None
        self.mR = None

class BST:
	
	def __init__(self):
		self.mRoot = None
		
	def Insert(self, item):
		if self.Exists(item):
			return False
		n = Node(item)
		self.mRoot = self.InsertR(n, self.mRoot)
		return True
		
	def InsertR(self, n, current):
		if current is None:
			current = n
		elif n.mItem < current.mItem:
			current.mL = self.InsertR(n, current.mL) # walk left
		elif n.mItem > current.mItem:
			current.mR = self.InsertR(n, current.mR) # walk right
		return current
			
	def Delete(self, item):
		if not self.Exists(item):
			return False
		self.mRoot = self.DeleteR(item, self.mRoot)
		return True
		
	def DeleteR(self, item, current):
		if item < current.mItem:
			current.mL = self.DeleteR(item, current.mL)
		elif item > current.mItem:
			current.mR = self.DeleteR(item, current.mR)
		else: # current is pointing to the node containing the item to be deleted
			if current.mL is None and current.mR is None: # no child case
				current = None
			elif current.mL is None and current.mR is not None: # one right child
				current = current.mR
			elif current.mL is not None and current.mR is None: # one left child
				current = current.mL
			else: # two children
				s = current.mR
				while s.mL is not None:
					s = s.mL
					
				current.mItem = s.mItem
				current.mR = self.DeleteR(s.mItem, current.mR) # start from current's right
		return current	
		
	def Exists(self, item):
		return self.ExistsR(item, self.mRoot)
		
	def ExistsR(self, item, current):
		if current == None:
			return False
		elif current.mItem == item:
			return True
		elif item < current.mItem:
			return self.ExistsR(item, current.mL)
		elif item > current.mItem:
			return self.ExistsR(item, current.mR)
	
	
	def Retrieve(self, item):
		return self.RetrieveR(item, self.mRoot)
		
	def RetrieveR(self, item, current):
		if current == None:
			return None
		elif current.mItem == item:
			return current.mItem
		elif item < current.mItem:
		    return self.RetrieveR(item, current.mL)
		elif item > current.mItem:
		    return self.RetrieveR(item, current.mR)
	
	
	def Traverse(self, callback):
		self.TraverseR(callback, self.mRoot)
			
	def TraverseR(self, callback, current):
		if current is not None:
			callback(current.mItem)
			self.TraverseR(callback, current.mL)
			self.TraverseR(callback, current.mR)
	
	
	def Size(self):
		total = [0]
		self.SizeR(total, self.mRoot)
		return total[0]		
		
	def SizeR(self, total, current):
		if current is not None:
			total[0] += 1
			self.SizeR(total, current.mL)
			self.SizeR(total, current.mR)