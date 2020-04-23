#!/usr/bin/env python3

import operator

def phone_book(people):
    for dude in sorted(people, key=operator.itemgetter('last','first')):
        print(f"{dude['last']}, {dude['first']}: {dude['email']}")


def main():
    people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
    {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
    {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}]
    phone_book(people)

if __name__ == "__main__":
    main()