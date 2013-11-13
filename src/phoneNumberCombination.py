#!/usr/bin/env python

"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

digit_letters = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z')    
    }


def phone_number_combination(digit_str):
    if not digit_str: return
    # check isdigit?
    letters = digit_letters[digit_str[0]]
    output = []
    
    q = []
    for l in letters:
        q.append((0, l))
        
    while q:
        pos, combination = q.pop()
        
        if pos != len(digit_str) - 1:
            for l in digit_letters[digit_str[pos + 1]]:
                q.append((pos + 1, combination + l))
        else:
            output.append(combination)
            
    return output


if __name__ == '__main__':
    print phone_number_combination('23')
    print phone_number_combination('2345')
    