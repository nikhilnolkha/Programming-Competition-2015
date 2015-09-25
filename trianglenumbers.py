# Developer - Nikhil Nolkha
# Release Date - 09/25/2015
# Problem Statement - https://projecteuler.net/problem=42
# The nth term of the sequence of triangle numbers is given by, t(n) = 0.5n(n+1); 
# so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word value is a triangle number then we shall call the word a triangle word.
        
# This function calculates the numeric value of a word
def word_value(word_string):
    word_list = list(word_string.upper())
    val = 0
    for x in word_list: 
        val = val + ord(x) - 64
    return val; 
            
# This function determines if a word is triangle word
def is_triangle_word(word):
    word_val = word_value(word)
    nvalue = 0
    n = 1
    while word_val >= nvalue:
        nvalue = 0.5*n*(n+1)
        if word_val == nvalue:
            return n
        n = n + 1
    return 0        
            
word = raw_input("Enter a word: ") #Assuming valid string is entered
triangle_number = is_triangle_word(word)
if triangle_number != 0:
    print "The word %-s is a triangle word with word value of t(%d)" %(word, triangle_number)
else:	
    print "The word %-s is not a triangle word" %word