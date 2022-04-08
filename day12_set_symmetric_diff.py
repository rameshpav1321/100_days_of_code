# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))
a = set1.difference(set2)
b = set2.difference(set1)
st = a.union(b)
lst = sorted(st)
for i in lst:
    print(i)
