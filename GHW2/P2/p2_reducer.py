import sys

current_key = None
current_values = set()

for line in sys.stdin:
    key, value = line.strip().split("\t")

    if key != current_key:
        if current_key:
            # Check for one-way relationships
            forward = {v for v in current_values if not v.endswith('*')}
            reverse = {v[:-1] for v in current_values if v.endswith('*')}
            one_way = forward - reverse

            if one_way:
                print '%s has one-way relationships with %s' % (current_key,', '.join(one_way))
        
        current_key = key
        current_values = set()

    current_values.add(value)

# Check for the last key
if current_key:
    forward = {v for v in current_values if not v.endswith('*')}
    reverse = {v[:-1] for v in current_values if v.endswith('*')}
    one_way = forward - reverse

    if one_way:
        print '%s has one-way relationships with %s' % (current_key,', '.join(one_way))