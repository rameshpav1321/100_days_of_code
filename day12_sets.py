def average(array):
    # your code goes here
    st = set(array)
    n = len(st)
    s = sum(st)
    return s/n


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
