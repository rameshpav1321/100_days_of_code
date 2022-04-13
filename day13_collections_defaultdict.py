# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
a = defaultdict(list)
b = []
for i in range(n):
    a[input()].append(i+1)
for i in range(m):
    b.append(input())
for i in b:
    if i in a:
        print(" ".join(map(str, a[i])))
    else:
        print(-1)
