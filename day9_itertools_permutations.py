# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, k = input().split()
k = int(k)
res = list(permutations(s, k))
lst = ["".join(i) for i in res]
lst.sort()
for i in lst:
    print(i)
