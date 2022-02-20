#include <ctype.h>

int count_vowels(char *str) {
	int count = 0;
	while (*str) {
		char ch = tolower(*str);
		if (ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u') {
			count++;
		}
		str++;
	}
	return count;
}