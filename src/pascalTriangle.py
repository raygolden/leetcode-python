#!/usr/bin/env python

#print out pascal triangle

"""Pascal's Triangle Total Accepted: 2401 Total Submissions: 7618 My Submissions
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]
"""

def pascalTriangle(n):
    output = []
    for i in range(0, n):
        row = []
        if i == 0:
            row.append(1)
        else:
            for j in range(0, i + 1):
                if j < 1 or j == i:
                    row.append(1)
                else:
                    row.append(output[i-1][j-1] + output[i-1][j])
                    
            
        output.append(row)
            
    return output


if __name__ == '__main__':
    print pascalTriangle(10)