def split_and_join(line):
    # write your code here
    lst = []
    lst = line.split()
    return "-".join(lst)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
