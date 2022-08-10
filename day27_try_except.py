# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as z:
        print("Error Code:", z)
    except ValueError as v:
        print("Error Code:", v)
