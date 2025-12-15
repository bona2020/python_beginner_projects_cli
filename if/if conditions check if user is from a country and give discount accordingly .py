uName =input('What\'s Your Name? ') .strip() .title()
uCountry =input('What\'s Your Country? ') .strip() .title()
cName = 'Python Course'
cPrice = 100
if uCountry == 'Egypt':
    print(f'Hello {uName} Because You are from {uCountry}')
    print(f'The course {cName} price is: ${cPrice-80}')
elif uCountry == 'Ksa':
    print(f'Hello {uName} Because You are from {uCountry.upper()}')
    print(f'The course {cName} price is: ${cPrice-60}')
elif uCountry == 'Kuwait':
    print(f'Hello {uName} Because You are from {uCountry}')
    print(f'The course {cName} price is: ${cPrice-50}')
else :
    print(f'Hello {uName} Because You are from {uCountry}')
    print(f'The course {cName} price is: ${cPrice-30}')