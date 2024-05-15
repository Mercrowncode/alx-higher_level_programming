#!/usr/bin/python3
# This program prints the ASCII lowercase alphabets except 'e' and 'q'. 
for i in range(97, 123):
    if chr(i) == 'q' or chr(i) == 'e': 
        continue
    print(chr(i).f(i), end='')