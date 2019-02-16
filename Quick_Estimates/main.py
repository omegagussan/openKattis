import sys
first = True
for i in sys.stdin:
  if not first:
    print(len(i.strip()))
  first = False
