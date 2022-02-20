calculator: calculator.o user_io.o
	g++ -o calculator calculator.o user_io.o

calculator.o: calculator.cpp user_io.h
	g++ -c calcuator.cpp

user_io.o: user_io.cpp user_io.h
	g++ -c user_io.cpp
