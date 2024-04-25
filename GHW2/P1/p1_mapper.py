import sys

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()
    if line:  # Check if line is not empty
        words = len(line.split())

        # Group the lines based on the number of words
        if words <= 2:  # Lines with 1 or 2 words
            print('%s\t%s' % (line, 3))  # Group 3
        elif words % 2 == 0:  # Lines with an even number of words
            print('%s\t%s' % (line, 1))  # Group 1
        else:  # Lines with an odd number of words
            print('%s\t%s' % (line, 2))  # Group 2
