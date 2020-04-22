#!/usr/bin/env python3
import itertools

def mysum(listone, listtwo):
    for item in itertools.chain(listone, listtwo):
        return print(listone + listtwo)

def main():
    listone = [1,2,3,]
    listtwo = [4,5,6]
    mysum(listone, listtwo)


if __name__ == "__main__":
    main()
