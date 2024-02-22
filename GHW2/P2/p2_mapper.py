import sys

for line in sys.stdin:
    line = line.strip()
    elements = line.split("->")

    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            print "%s\t%s" % (elements[i],elements[j]) 
            print "%s\t%s*" % (elements[j],elements[i]) 