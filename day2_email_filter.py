import re


def fun(s):
    # print(s)
    split_list = re.split('[@.]', s)
    # print(split_list)
    if(len(split_list) == 3):
        if(re.match("^[A-Za-z0-9_-]*$", split_list[0]) and len(split_list[0]) != 0):
            if(re.match("^[A-Za-z0-9]*$", split_list[1]) and len(split_list[1]) != 0):
                if(re.match("^[A-Za-z]*$", split_list[2]) and len(split_list[2]) <= 3):
                    return True
    return False

    # return True if s is a valid email, else return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
