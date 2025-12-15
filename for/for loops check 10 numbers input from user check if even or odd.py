myNumbers =[]
for n in range(10):
    number=int(input('Check any Number Even/Odd: '))
    myNumbers.append(number)
    print(f'{number} is Even' if number % 2 == 0 else f'{number} is Odd.')
else:
    print('Loop is finished')
print(myNumbers)
print('='*50)
for number in myNumbers :
    print(f'{number} is Even' if number % 2 == 0 else f'{number} is Odd.')