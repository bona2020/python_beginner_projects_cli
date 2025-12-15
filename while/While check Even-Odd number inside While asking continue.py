#While check Even/Odd number inside While asking continue :
while True:
    x = input('Check a number: ').strip()
    if not x :
        print('Cant be Empty..')
        continue
    elif not x.isdigit():
        print('Only Numbers Please.')
        continue
    x = int(x)
    if x % 2 == 0:
        print('Even')
    else:
        print('Odd')
    while True:
        again = input('Continue? Y/N: ').strip().lower()
        if again not in ['y','n','yes','no']:
            print('Invalid Response, Please choose Y/N.')
            continue
        else:
            break
    if again in ['n','no']:
        print('Thank you Done.')
        break