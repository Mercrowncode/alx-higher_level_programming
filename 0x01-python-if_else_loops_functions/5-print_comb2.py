#!/usr/bin/python3
#This program prints the numbers from 00 to 99, with each number formatted as a two-digit number and separated by commas. 
for num in range(0, 99):
    print("{:02d}".format(num), end=',')
print("{:02d}".format(num + 1))