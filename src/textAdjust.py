#!/usr/bin/env python
'''
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''

def spacing(text, start, end, length):
    space = " "
    # even out the empty space
    space_tobe_filled = length - len(''.join(text[start:end]))
    if end - start - 1 != 0:
        space_each = space_tobe_filled / (end - start -1)
        space_mod = space_tobe_filled % (end - start - 1)
    else:
        space_each = space_tobe_filled
        space_mod = 1
        
    if space_mod > 0:
        line = text[start] + (space * (space_each + 1)) + (space * space_each).join(text[start + space_mod:end])

    else:
        line = (space * space_each).join(text[start:end])
            
    return line
                

def textJustication(text, length):
    tmp = ''
    space = " "
    output = []
    start = 0
    i = start
    while i < len(text):
        tmp = space.join(text[start:i + 1])
        l = len(tmp)
        if l < length:
            i += 1
            if i == len(text):
                line = spacing(text, start, i, length)
                output.append(line)
                
            else:
                continue
        elif l == length:
            output.append(tmp)
            start = i + 1
            i += 1
        else:
            line = spacing(text, start, i, length)
            output.append(line)
            
            start = i
    
            
    return output

print textJustication(["This", "is", "an", "example", "of", "text", "just", 'something', 'w'], 16)
        
print textJustication( ["What","must","be","shall","be."], 12)