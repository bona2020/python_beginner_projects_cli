import getpass

tries = 3
mainPassword = '123'

while tries > 0:
    inputPassword = getpass.getpass('Write your password: ')
    if inputPassword == mainPassword:
        print('✅ Correct password')
        break
    tries -= 1
    if tries == 0:
        print('❌ Access Denied')
    else:
        print(f"Wrong password. {'Last' if tries == 1 else tries} attempts left")
        print('=' * 80)
