#!/usr/bin/env python3

def even_odd_sum(sequence):
    #takes a list or tuple of numbers
    #return a two-element list
    #with sum of even indexed numbers
    #with sum of odd indexed numbers
    return print([sum(sequence[0::2]), sum(sequence[1::2])])

def plus_minus(sequence):
    #takes a list or tuple of numbers
    #return a sum
    #alternate addition and subtraction 
    #in order of the elements in the list
    return print(sequence[0::1])

def main():
    sequence = [10, 20, 30, 40, 50, 60]
    even_odd_sum(sequence)
    plus_minus(sequence)

if __name__ == "__main__":
    main()