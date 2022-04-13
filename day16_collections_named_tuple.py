# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
total_sum = 0
student = namedtuple('student', input())
for i in range(n):
    # tmp1=student._make(input().split())
    tmp = student(*input().split())
    total_sum += int(tmp.MARKS)
print("{0:.2f}".format(total_sum/n))
