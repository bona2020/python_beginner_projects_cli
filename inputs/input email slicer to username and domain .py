done = 'n' 
while done != 'y' :
    email = input('Please enter your Email: ')
    username = email[:email.index('@')]
    domain = email[email.index('@')+1:]
    print(f'Your Username is {username} and your Domain is {domain}')
    done = input('Are you Done? Y/N ') .strip() .lower()
    print('='*50)
else: 
    print('Program Exited Successfully')
    print('='*50)