#include <stdio.h>

int count_vowels(char *str) {
  int length = 0;
  int vowels = 0;
  while (str[length] != 0) {
    length++;

    char ch = str[length];
    if (ch == 'a') {
      vowels++;
    }
  }

  return vowels;
}
