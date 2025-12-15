myName = input('What\'s your name? ').title()
for n in range(len(myName)):
    print(f'"{myName[n]}" is in the index of "{n}"')
else:
    print(f'Your name is "{myName}"')