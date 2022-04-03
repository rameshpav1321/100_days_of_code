# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s, k = input().split()
k = int(k)
s = list(s)
s.sort()
res = []
lst = []
fin = []
for i in range(1, k+1):
    res.append(list(combinations(s, i)))
    lst.append(["".join(j) for j in res[i-1]])
for i in range(len(lst)):
    fin += lst[i]
for i in fin:
    print(i)
