from linked_list import Blob, Student
import time

gTotalAge = 0

def AddAges(s):
	global gTotalAge
	gTotalAge += int(s.getAge())
	

def main():
	global gTotalAge
	slist = Blob()
	
	#insert
	t1 = time.time()
	fin = open("InsertNames.txt", "r")
#	fin = open("testinsertnames.txt", "r")
	for line in fin:
		words = line.split()
		s = Student(words[0], words[1], words[2], words[3], words[4])
		ok = slist.Insert(s)
		if not ok:
			print("Could not insert student with SSN", s.getFName())
	fin.close()
	
	t2 = time.time()
	t = t2-t1
	print("Insert time:", round(t, 2), "seconds\n")
	
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
	fin = open("DeleteNames.txt", "r")
#	fin = open("testdeletenames.txt", "r")
	for line in fin:	
		dummyStudent = Student("", "", line.strip(), "", "0")
		ok = slist.Delete(dummyStudent)
		if not ok:
			print("Could not delete student with SSN", dummyStudent.getSSN())
	fin.close()
	
	t2 = time.time()
	t = t2-t1
	print("Delete time:", round(t, 2), "seconds\n")
	
	#retrieve
	totalAge = 0
	totalCount = 0
	t1 = time.time()
	fin = open("RetrieveNames.txt", "r")
#	fin = open("testretrievenames.txt", "r")
	for line in fin:	
		dummyStudent = Student("", "", line.strip(), "", "0")
		actualStudent = slist.Retrieve(dummyStudent)
		if actualStudent is None:
			print("Could not retrieve student with SSN", dummyStudent.getSSN())
		else:
			totalAge += int(actualStudent.getAge())
			totalCount += 1

	t2 = time.time()
	t = t2-t1
	print("\nRetrieve time:", round(t, 2), "seconds")
	print("The average age is", round(totalAge/totalCount, 2))

main()