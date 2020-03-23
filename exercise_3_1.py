#!/usr/bin/env python3

def firstlast(seq):
    return seq[:1] + seq[-1:]


def main():
    seq = "cadbv"
    print(firstlast(seq))

if __name__ == "__main__":
    main()