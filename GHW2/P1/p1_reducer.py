import sys
import random

# Set seed for debugging
random.seed(1)

# Initialize lists to store results
even, odd, one_two = [], [], []

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()
    # Check if line contains a tab character
    if '\t' in line:
        sentence, group = line.split('\t', 1)

        # Group the sentences based on the group number
        if group == '1':
            if len(even) < 66:
                even.append(sentence)
            else:
                index = random.randint(0, 65)
                even[index] = sentence
        elif group == '2':
            if len(odd) < 67:
                odd.append(sentence)
            else:
                index = random.randint(0, 66)
                odd[index] = sentence
        elif group == '3':
            if len(one_two) < 67:
                one_two.append(sentence)
            else:
                index = random.randint(0, 66)
                one_two[index] = sentence
    else:
        # Skip lines that do not conform to expected format
        continue

# Combine the results and print them
result = even + odd + one_two
for sentence in result:
    print('%s' % sentence)
