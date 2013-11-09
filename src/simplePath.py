#!/usr/bin/env python

"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""

def simplePath(path):
    dir = path.split("/")
    stack = []
    
    while dir:
        t = dir.pop(0)
        if t == '.' or t == '':
            # stay the same ignore
            continue
        elif t == '..':
            # go upper level
            if stack:
                stack.pop()
        else:
            stack.append(t)
            
    return "/" + '/'.join(stack)
    
 
if __name__ == '__main__':   
    print simplePath('/home/')
    print simplePath("/a/./b/../../c/")
    print simplePath("/../")
    print simplePath("/home//foo/")
    print simplePath('/')
            