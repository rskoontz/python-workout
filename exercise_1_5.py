#!/usr/bin/env python3

deci_num = 0
hexi_num = input("Enter a hexidecimal number that will be converted into a decimal integer: ")

for exponent, digit in enumerate(reversed(hexi_num)):
    deci_num += int(digit, 16) * (16 ** exponent)
print(deci_num)





#for index, one_letter in enumerate('abcd'):
#    print(f"{index}: {one_letter}")

