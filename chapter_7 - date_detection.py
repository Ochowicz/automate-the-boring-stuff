#! python3

import pyperclip
import re

date_regex = re.compile(r'(0[1-9]|[1-2][1-9]|30|31)(/)(0[1-9]|11|12)(/)([1-2]\d{3})')

text = str(pyperclip.paste())
valid_date = []
print(date_regex.findall(text))
for tuples in date_regex.findall(text):
    day, _, mounth, _, year = tuples
    if mounth == '04' or '4' or '06' or '6' or '09' or '9' or '11':
        if int(day) < 31:
            date = day + '/' + mounth + '/' + year
            print(date)
    elif mounth == '01' or '1' or '03' or '3' or '05' or '5' or '07' or '7' or '08' or '8' or '10' or '12':
        if int(day) < 32:
            date = day + '/' + mounth +'/' + year
            print(date)
    elif mounth == '02' or '2':
        if int(year)%400 == 0:
            if int(day) < 30:
                date = day + '/' + mounth + '/' + year
                print(date)
        elif int(year)%100 == 0:
            if int(day) < 29:
                date = day + '/' + mounth + '/' + year
                print(date)
        elif int(year)%4 == 0:
            if int(day) < 30:
                date = day + '/' + mounth + '/' + year
                print(date)
    else:
        valid_date += day + '/' + mounth +'/' + year

#pyperclip.copy(valid_date)
print('Valid date copied to clipboard:')
print('Valid Dates:')
print(valid_date)

