def print_formatted(number):
    # your code goes here
    l = len(str(bin(number)[2:]))
    for i in range(1, number+1):
        print(
            f"{str(i).rjust(l)} {str(oct(i)[2:]).rjust(l)} {format(i,'X').rjust(l)} {str(bin(i)[2:]).rjust(l)}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
