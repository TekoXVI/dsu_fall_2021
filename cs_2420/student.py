import time

class Student:

    def __init__(self, lname, fname, ssn, email, age):
        
        self.lname = lname
        self.fname = fname
        self.ssn = ssn
        self.email = email
        self.age = age


def main():
    students = []
    
    t1 = time.time()
    
    file = open('InsertNames.txt', 'r')
#    file = open('testinsertnames.txt', 'r')
    
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        name = []
        for word in line.split(' '):
            name.append(word)
        s = Student(name[0], name[1], name[2], name[3], name[4])

        if students == []:
            students.append(s)
        else:
            dup = False
            for student in students:
                if student.ssn == s.ssn:
                    print('Duplicate:', s.fname, s.lname)
                    dup = True
            if dup == False:
                students.append(s)
                
    t2 = time.time()
    
    print('Names inserted:', len(students))
    print('Insert time:', round(t2-t1, 2), "seconds")
    print()

    
    t1 = time.time()
    age = 0
    for student in students:
        age += int(student.age)
    age /= len(students)
    t2 = time.time()
    
    print('Average age:', round(age, 2)) 
    print('Time:', round(t2-t1, 2), "seconds")
    print()

#delete names
    t1 = time.time()
    
    file = open('DeleteNames.txt', 'r')
#    file = open('testdeletenames.txt', 'r')

    lines = file.readlines()

    count = 0
    for line in lines:
        removed = False
        for student in students:
            if line.strip() == student.ssn:
                students.remove(student)
                count += 1
                removed = True
        if not removed:
            print("Not deleted:", line.strip())
        
    
    t2 = time.time()
    print('Names deleted:', count)
    print('Names:', len(students))
    print('Delete time:', round(t2-t1, 2), "seconds")
    print()
    

#retrieve names
    t1 = time.time()

    file = open('RetrieveNames.txt', 'r')
#    file = open('testretrievenames.txt', 'r')

    lines = file.readlines()
    age = 0
    count = 0
    for line in lines:
        retrieved = False
        for student in students:
            if line.strip() == student.ssn:
                age += int(student.age)
                count += 1
                retrieved = True
        if not retrieved:
            print("Not retrieved:", line.strip())
    age /= count
                

    t2 = time.time()
    print('Average age:', round(age, 2))
    print('Names retrieved:', count)
    print('Names:', len(students))
    print('Retrieve time:', round(t2-t1, 2), "seconds")
    print()


main()