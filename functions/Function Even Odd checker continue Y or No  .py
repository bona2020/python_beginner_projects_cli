def check():
    n= input('Check a Number: ')
    if not n :
        print('Can’t be empty. Please enter a number.')
        return check()
    elif not n.isdigit():
        print('Only whole numbers allowed. Try again.')
        return check()
    else:
        n= int(n)
        print(f'"{n}" is Even'if n % 2 ==0 else f'"{n}" is Odd')
        again = input('Continue Y/N: ').strip().lower()
        while again not in ['y','yes','no','n']:
            again=input('Please enter Y or N to continue: ').lower().strip()
        if again in ['y','yes']:
            return check()
        elif again in ['n','no']:
            print('Thank you for using the Even/Odd Checker! Done.')
check()