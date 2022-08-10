# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    key = True
    try:
        var = re.compile(input())
    except re.error:
        key = False
    print(key)
