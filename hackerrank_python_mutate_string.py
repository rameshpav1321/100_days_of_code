def mutate_string(string, position, character):
    # mutated=string[:position]+character+string[position+1:]
    lst = list(string)
    lst[position] = character
    mutated = "".join(lst)
    return mutated


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
