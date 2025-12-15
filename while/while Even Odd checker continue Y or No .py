print('Welcome to the Even/Odd Checker!')
while True :
    n = input('check a number: ').strip()
    if not n :
        print('Can’t be empty. Please enter a number.')
        continue
    elif not n.isnumeric():
        print('Only numbers allowed. Try again.')
        continue
    n = int(n)
    print(f'"{n}" is Even'if n % 2 ==0 else f'"{n}" is Odd')
    again = input('Continue Checking? Y/N: ').lower().strip()
    while again not in ['y','yes','n','no'] :
        again = input('Please enter Y or N to continue.: ').lower().strip()
    if again in ['n','no']:
        print('Thank you for using the Even/Odd Checker! Done.')
        break