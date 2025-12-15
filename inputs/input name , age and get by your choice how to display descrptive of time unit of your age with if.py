name = input('What is your Name? ').strip().title()
age = int(input('What\'s your Age? ').strip())
choice = input('''Please choose how you want to dispaly your Age:
[ Years = Y, Months = M, Weeks = W, Days = D, HOURS = H, MINUTES = MIN, SECONDS = S]
: ''').strip().lower()
months = age*12
weeks = age *52
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print('='*80)
if choice == 'y' or choice =='year' or choice == 'years':
    print(f'Hi, {name} you have lived for {age:,} Years.')
elif choice == 'm' or choice =='month' or choice == 'months':
    print(f'Hi, {name} you have lived for {months:,} Months.')
elif choice == 'w' or choice =='week' or choice == 'weeks':
    print(f'Hi, {name} you have lived for {weeks:,} Weeks.')
elif choice == 'd' or choice =='day' or choice == 'days':
    print(f'Hi, {name} you have lived for {days:,} Days.')
elif choice == 'h' or choice =='hour' or choice == 'hours':
    print(f'Hi, {name} you have lived for {hours:,} Hours.')
elif choice == 'min' or choice =='minute' or choice == 'minutes':
    print(f'Hi, {name} you have lived for {minutes:,} Minutes.')
elif choice == 's' or choice =='second' or choice == 'seconds':
    print(f'Hi, {name} you have lived for {seconds:,} Seconds.')
else:
    print('Wrong choice please choose again')
print('='*80)