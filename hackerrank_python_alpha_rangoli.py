def print_rangoli(size):
    # your code goes here
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    sub_alpha = alphabets[:size]
    iterable = list(range(size))
    iterable = iterable[:-1]+iterable[::-1]
    for i in iterable:
        right = sub_alpha[-(i+1):]
        left = right[::-1]
        rangoli = left[:-1]+right
        print("-".join(rangoli).center(size*4-3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
