int main() {
  int i, n;
  // set max reps
  n = 7
  // for(init; test; increment) {
  //    body;
  // }
  // i = i + 1;
  // i += 1;
  // i++;
  for(i = 0; i < n; i = i + 1) {
      std::cout << i << "Hello world" << std::endl;
  }

  return 0;
}

int i = 0, n = 7;

for(; i < n;) {
  i++;
  std::cout << i << "Hello world" << std::endl;
}

for(i=0;;) {
  i++;

  if(i > 1000) {
    break;
  }
}


while(i < n) {
  std::cout << "hello" << std::endl;
  i++;
}

while(i < n) {
  i = getInteger(std::cin, std::cout, "prompt");
  std::cout << "thanks for the" << i << endl;
}



#include <vector>

int main() {
  // [2,3,5,7,11,13]
  std::vector<int> primes; // start with 0 slots available
  std::vector<int> primes_less_inneficient(6); // start with 6 slots available
  std::vector<int> primes_initialized = {2,3,5,7,11,13}; // start with 6 vlaues

  primes.push_back(2);
  // same as append in py
  primes.push_back(3); // add to the end of a vector
  primes.push_back(5);
  primes.push_back(7);
  primes.push_back(11);
  primes.push_back(13);

  primes_less_inefficient[0] = 2; // assign to a slot
  primes_less_inefficient[1] = 3;
  primes_less_inefficient[2] = 5;
  primes_less_inefficient[3] = 7;
  primes_less_inefficient[4] = 11;
  primes_less_inefficient[5] = 13;


	// change the size of a vector
	primes.resize(100);

	unsigned int i;
	for(i = 0; i < primes_less_inefficient.size(); i++) {
		std::cout << primes_less_inefficient[i] << " ";
	}
	std::cout << std::endl;
	
  return 0;
}


// point.h

#ifndef _POINT_H_
#define _POINT_H_

class Point {
public:
	Point(); // default constructor
	Point(const int& x_in, const int& y_in);
	int getX() const;
	int getY() const;
	void setX(int x_in);
	void setY(int y_in);

private:
	int x;
	int y;	
};


#endif

// point.cpp

#include "Point.h"


int main () {
	Point p1;
	Point p2(3,8);
	std::cout << p1.getX() << std::endl;
	std::cout << p1.getY() << std::endl;
	// ...
	p1.setY(1);
	std::cout << p1.getY() << std::endl;
	
}


// Point.cpp

#include "Point.h"

Point::Point() 
	: x(0), y(0) {
	// x = 0;
	// y = 0;
}
Point::Point(const int& x_in, const int& y_in) 
	: x(x_in), y(y_in) {
	// x = x_in;
	// y = y_in;
}
int Point::getX() const {
	return x;
}
int Point::getY() const {
	return y;
}
void Point::setX(int x_in) {
	x = x_in;
}
void Point::setY(int y_in) {
	y = y_in;
}


// Point3D.h

#ifndef _POINT3D_H_

#include "Point.h"

class: Point3D: public Point {
	public:
		Point3D();
		Point3D(const double& x, const double& y, const double& z);

		double getZ() const;
		void setZ(const double& z);

	private:
		double mZ;
	}




// Point3D.cpp

#include "Point.h"

Point3D::Point3D()
	: Point(),mZ(0.0) {
	}

Point3D::Point3D(const double& x, const double& y, const double& z)
	: Point(x, y), mZ(z){
	}

double Point3D::getZ() const {
	return mZ;
}

void Point3D::setZ(const double& z) {
	mZ = z;
}




#include <iostream>

class BigData {
public:
	BigData(int& v);
	void display() const;
private:
	int& mValue;
};

BigData::BigData(int& v)
	: mValue(v){
	}
void BigData::display() const {
	std::cout << mValue << std::endl;
}

void display(const int& v2) { // const makes it read v2 but not able to change it
	std::cout << v2 << std::endl;
}

void change(int& value) {
	value = 13;
}

int main() {
	int x = 7; 
	change(x); // changes x to 13
	display(x);

	BigData d(x);
	d.display();
	x = 17;
	
	return 0;
}




#include <vector>
#include <map>

int main() {
	std::vector<int> nums;
	std::map<std::string, int> words_to_numbers;
	std::pair<std::string, int> value;
		
	// store "one" -> 1
	words_to_numbers["one"] = 1;
	words_to_numbers.insert("one", 1);
	// store "two" -> 2
	value.first = "two"
	value.second = 2
	words_to_numbers.insert(value);

	// if key in dict:
	if (words_to_numbers.find("four") != words_to_numbers.end()) {
		std::cout << "four" << std::endl;
	} else {
		std::cout << "!four" << std::endl;
	}
	// for key in dictionary
	std::map<std::string, int>::iterator it;
	for (it = words_to_numbers.begin(); it != words_to_numbers.end(); it++) {
		std::cout << it->first << " " << it->second << std::endl;
	}
	
}










































.