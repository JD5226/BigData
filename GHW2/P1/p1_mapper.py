import sys

# devide input into lines
for line in sys.stdin:
    line = line.strip()
    words = len(line.split())
    
    # gether groups
    if words <= 2: # line with 1 or 2 words
        print '%s\t%s' % (line, 3) # group 3
    elif words % 2 == 0: # line with even number of words
        print '%s\t%s' % (line, 1) # group 1
    else: # line with odds number of words
        print '%s\t%s' % (line, 2) # group 2
    