n, m = map(int, input().split())
mid = n//2
str = "WELCOME"
for i in range(mid):
    print(('.|.'*((2*i)+1)).center(m, '-'))
print(str.center(m, '-'))
for i in reversed(range(mid)):
    print(('.|.'*((2*i)+1)).center(m, '-'))
