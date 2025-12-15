tries = 3
mainPassword = '123'
while tries > 0:
    inputPassword = input('write your password: ')
    if inputPassword != mainPassword:
        print(f'Incorrect password "{'last' if tries == 1 else tries}" attempts left')
    else:
        print('Correct password')
        break
    tries -=1
    if tries == 0:
        print('Access Denied Please try again later!')