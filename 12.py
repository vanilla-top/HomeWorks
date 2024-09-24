#обшщии баллы
bal = 300

s1 = int(input('математика: '))
s2 = int(input('физика: '))
s3 = int(input('биология: '))
res = s1 + s2 + s3
if res >= bal:
    print('поступил')
else:
    print('не поступил')