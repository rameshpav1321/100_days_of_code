def merge_the_tools(string, k):
    # your code goes here
    lst = []
    for i in range(0, len(string), k):
        lst.append(string[i:i+k])
    for i in range(len(lst)):
        lst[i] = "".join(dict.fromkeys(lst[i]))
        print(lst[i])


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# alternate def


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        uniq = ''
        for c in string[i: i+k]:
            if (c not in uniq):
                uniq += c
        print(uniq)
