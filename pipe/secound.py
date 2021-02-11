import sys

for line in sys.stdin:
    if line.rstrip() != "cc":
        print(line.rstrip())
