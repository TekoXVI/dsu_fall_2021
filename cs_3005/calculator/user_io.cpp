#include <iostream>
#include <string>
#include "user_io.h"

int getInteger(std::istream& input_stream, std::ostream& output_stream, const std::string& prompt) {
  int response;
  // display prompt to output stream
  output_stream << prompt;
  // read response from input stream
  input_stream >> response;
  // return the response
  return response;
}
