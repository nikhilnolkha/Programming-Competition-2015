# Developer - Nikhil Nolkha
# Release Date - 09/24/2015
# Problem Statement - https://projecteuler.net/problem=41
# n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
import math
import itertools
        
# This function determines whether a number is pan-digital or not
def ispandigital(n):
    arr_digits = []
    while n > 0:
        r = n % 10
        if r in arr_digits:
            return 0
        else:
            arr_digits.append(r)
            n = n / 10
    return 1;
        
# This function determines whether a number is prime or not
def isprime(n):
    start = int(math.ceil(n/3) + 1)
    for i in range(3, start, 2):
        if n % i == 0:
            return 0
    return 1
    
# This function finds the largest n-digit pan-digital prime number
def maxpandigitalprime(n):
    uplimit = pow(10, n) - 1
    for i in itertools.count(uplimit, -2):
        if ispandigital(i) and isprime(i):
            return i
        elif i < pow(10, (n-1)):
            return 0
            
n = int(raw_input("Enter number of digits: ")) #Assuming valid integer value is entered
if n < 0 or n > 10 or n == 0:
    print "Enter valid number of digits from 1 to 10"
else:
    max_n_digit_pp = maxpandigitalprime(n)
    if max_n_digit_pp != 0:
        print "The largest %d-digit pan-digital prime number is %d" %(n, max_n_digit_pp)
