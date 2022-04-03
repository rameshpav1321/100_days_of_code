# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
lst1 = input().split()
lst1 = [int(x) for x in lst1]
lst2 = input().split()
lst2 = [int(x) for x in lst2]
print(*list(product(lst1, lst2)))
