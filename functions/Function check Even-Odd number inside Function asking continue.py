# Fuction check Even/Odd number inside Function asking continue :
def check(again='y'):
    if again in ['n','no']:
        return 'Thank you Done'
    number = input('check a number: ')
    if not number :
        print('Cant be empty..')
        return check()
    elif not number.isdigit():
        print('Only Numbers please.')
        return check()
    number = int(number)
    print('Even'if number % 2 == 0 else 'Odd')
    def ask():
        answer = input('Continue? Y/N: ').lower().strip()
        if answer not in ['y','yes','n','no']:
            print('Invalid Response, Please choose Y/N')
            return ask()
        return answer
    again = ask()
    return check(again)
print(check())