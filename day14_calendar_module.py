# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month, date, year = input().split()
a = calendar.weekday(int(year), int(month), int(date))
weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY',
            'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(weekdays[a])
