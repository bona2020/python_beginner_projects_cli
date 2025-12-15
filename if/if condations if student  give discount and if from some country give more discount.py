uName = input('What is your name? ') .strip() .capitalize()
isStudent = input('Are you a Student? Y/N ') .strip() .capitalize()
uCountry = input('Where are you From? ') .strip() .capitalize()
cName = 'Python Course'
cPrice = 100
if isStudent == 'Yes' or isStudent == 'Y' :cPrice -=10
if uCountry == 'Egypt' or uCountry == 'Djibouti' or uCountry =='Ksa'or uCountry == 'Qatar':
    print(f'Hi {uName} Because U R from {uCountry}')
    print(f'The course "{cName}" price is: ${cPrice-80}')
        
elif uCountry == 'Kuwait'or uCountry == 'Bahrain':
    print(f'Hi {uName} Because U R from {uCountry}')
    print(f'The Course "{cName} Price is: ${cPrice-50}')
else:
    print(f'Hi {uName} Becaues You are from {uCountry}')
    print(f'The course {cName} price is: ${cPrice-30}')