def fiz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    return number


print(fiz_buzz(15))

s = list(range(1, 4))
print(s)
