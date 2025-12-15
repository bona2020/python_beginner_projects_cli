a = int(input('Type the number to check if it is Even/Odd: '))
while a != 0:
    print('='*80)
    print(f'{a} is Even Number'if a % 2 == 0 else f'{a} is Odd Number')
    print('='*80)
    a = int(input('Type the number to check if it is Even/Odd: '))
else:
    print('='*80)
    print(f'{a} is Zero')
