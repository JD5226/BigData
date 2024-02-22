import sys
import random

#set seed for debugging
random.seed(1)

# store result only
even = [] # 66
odd = [] # 67
one_two = [] # 67

for line in sys.stdin:
    line = line.strip()
    sentence, group = line.split('\t', 1)

    if group == '1':
        if len(even)<66:
            even.append(sentence)
        else:
            index = random.randint(0,66)
            even[index] = sentence
    elif group == '2':
        if len(odd)<67:
            odd.append(sentence)
        else:
            index = random.randint(0,67)
            odd[index] = sentence
    elif group == '3':
        if len(one_two)<67:
            one_two.append(sentence)
        else:
            index = random.randint(0,67)
            one_two[index] = sentence
    else:
        continue

result = even+odd+one_two
for i in result:
    print '%s' % (i)
