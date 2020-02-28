#!/usr/bin/env python3

def mysum(*numbs):
    result = 0
    for item in numbs:
            result += item
    return result
print(mysum(10,20,30,40,50))