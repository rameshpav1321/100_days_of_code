# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
arr = list(map(int, input().split()))
happinness = 0
like = set(map(int, input().split()))
dislike = set(map(int, input().split()))
for i in arr:
    if(i in like):
        happinness += 1
    if(i in dislike):
        happinness -= 1
print(happinness)
