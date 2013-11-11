#!/usr/bin/env python

# given a list of words, write a function which
# takes in the list, and groups the words together
# according to which ones are anagrams of eachother
# e.g.
# input = ["art", "rat", "bats", "banana", "stab", "tar"]
# output = [["art", "rat", "tar], ["bats", "stab"], ["banana"]]


def groupAnagrams(input):
    new_input = [(elm, sorted(elm)) for elm in input]
    new_input = sorted(new_input, key=lambda x:x[1])
    
    output = []
    cur_ana = new_input[0][1]
    group = []
    for elm, ana in new_input:
        if ana == cur_ana:
            group.append(elm)
        else:
            output.append(group)
            cur_ana = ana
            group = [elm]
            
    output.append(group)       
    return output


if __name__ == '__main__':
    print groupAnagrams(["art", "rat", "bats", "banana", "stab", "tar"])