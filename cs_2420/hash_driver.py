from hash_table import Blob, Student
import time

gTotalAge = 0

def AddAges(s):
	global gTotalAge
	gTotalAge += int(s.getAge())
	

def main():
	global gTotalAge
	slist = Blob(300000)
	
	#insert
	t1 = time.time()
	fin = open("InsertNamesMedium.txt", "r")
	# fin = open("InsertNames.txt", "r")
	# fin = open("testinsertnames.txt", "r")
	icount = 0
	for line in fin:
		words = line.split()
		s = Student(words[0], words[1], words[2], words[3], words[4])
		ok = slist.Insert(s)
		if not ok:
			# print("Could not insert student with SSN", s.getSSN())
			icount += 1
	fin.close()
	
	t2 = time.time()
	t = t2-t1
	print("Insert time:", round(t, 2), "seconds")
	print("Insert fails:", icount, "\n")
	
	#traverse
	gTotalAge = 0
	
	t1 = time.time()
	slist.Traverse(AddAges)
	t2 = time.time()
	t = t2-t1
	print("Traverse time:", round(t, 2), "seconds")
	print("The average age is", round(gTotalAge/slist.Size(), 2), "\n")

	#delete
	t1 = time.time()
	fin = open("DeleteNamesMedium.txt", "r")
	# fin = open("DeleteNames.txt", "r")
	# fin = open("testdeletenames.txt", "r")
	dcount = 0
	for line in fin:	
		dummyStudent = Student("", "", line.strip(), "", "0")
		ok = slist.Delete(dummyStudent)
		if not ok:
			# print("Could not delete student with SSN", dummyStudent.getSSN())
			dcount += 1
	fin.close()
	
	t2 = time.time()
	t = t2-t1
	print("Delete time:", round(t, 2), "seconds")
	print("Delete fails:", dcount, "\n")
	
	#retrieve
	totalAge = 0
	totalCount = 0
	t1 = time.time()
	fin = open("RetrieveNamesMedium.txt", "r")
	# fin = open("RetrieveNames.txt", "r")
	# fin = open("testretrievenames.txt", "r")
	rcount = 0
	for line in fin:	
		dummyStudent = Student("", "", line.strip(), "", "0")
		actualStudent = slist.Retrieve(dummyStudent)
		if actualStudent is None:
			# print("Could not retrieve student with SSN", dummyStudent.getSSN())
			rcount += 1
		else:
			totalAge += int(actualStudent.getAge())
			totalCount += 1
    
	t2 = time.time()
	t = t2-t1
	# gTotalAge = 0
	# slist.Traverse(AddAges)
	print("Retrieve time:", round(t, 2), "seconds")
	print("The average age is", round(totalAge/totalCount, 2))
	print("Retrieve fails:", rcount, "\n")

main()