# Developer - Nikhil Nolkha
# Release Date - 10/02/2015
# trianglenumbers.py
# Problem Statement - https://projecteuler.net/problem=42
# The nth term of the sequence of triangle numbers is given by, t(n) = 0.5n(n+1); 
# so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word value is a triangle number then we shall call the word a triangle word.
# Determine how many words in a file are triangle words
    
# This function determines the number of triangle words in a file
def cnt_triangle_word(file_name):
    txt = open(file_name)
    arr_words = txt.read().replace('"','').replace(' ','').split(',')
    total_words = len(arr_words)
    triangle_word_cnt = 0
    for i in arr_words:
        letter_list = list(i.upper())
        word_val = 0
        for x in letter_list: 
            word_val = word_val + ord(x) - 64
        nvalue = 0
        n = 1
        while word_val >= nvalue:
            nvalue = 0.5*n*(n+1)
            if word_val == nvalue:
                triangle_word_cnt = triangle_word_cnt + 1
            n = n + 1
    print "Of the total %d words in the file %-s, %d words are triangle word" %(total_words,file_name,triangle_word_cnt)

print "Type the file name:" 
filename = raw_input("> ")
cnt_triangle_word(filename)