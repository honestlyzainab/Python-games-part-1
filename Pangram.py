#we want to check if a phone number is pangram or not?

phone_number=input('Enter your phone number: ')
#989-912-3789
number={
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0,
}

for num in phone_number:
    if num in number:
        number[num]=1
print(number)
pangram=True

for num in number.values():
    if num ==0:
        pangram=False
        break
if pangram:
    print('Yes this phone number is a pangram!')
else:
    print('no, this phone number is not a panagram')
