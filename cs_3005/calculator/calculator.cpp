#include <iostream>
#include <string>
#include "user_io.h"

int main() {
  // add x and y together, display the result
  int x;
  int y;
  int z;

  //x = 1;
  x = getInteger(std::cin, std::cout, "Please give me an integer: ");
  y = 2;
  z = x + y;

  std::cout << "The result is  ";
  std::cout << z;
  std::cout << ".";
  std::cout << std::endl;

  return 0;
}
