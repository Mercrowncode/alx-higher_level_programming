#!/usr/bin/python3

def no_c(my_string):
    new_String = my_string.translate({ord('c'): None})
    new_String = new_String.translate({ord('C'): None})
    return new_String
