import sys

for line in sys.stdin:
    line = line.strip()
    start = 0
    while True:
        end = line.find("->", start)
        if end == -1:  # no more "->"
            break
        a = line[start:end]
        next_start = line.find("->", end + 2)
        if next_start == -1:
            b = line[end + 2:]
        else:
            b = line[end + 2:next_start]
        if a < b:
            print("%s\t%s" % (a, b))
        else:
            print("%s\t%s*" % (b, a))
        start = end + 2
