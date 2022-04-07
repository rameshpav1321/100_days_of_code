# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
shoe_count = int(input())
lst = input().split()
size_list = Counter(lst)
# print(size_list)
required_size = {}
customer_count = int(input())
money = 0
for i in range(customer_count):
    a, b = input().split()
    if(a in size_list and size_list[a] != 0):
        money += int(b)
        # print(money)
        size_list[a] -= 1
        # print(size_list)
print(money)
