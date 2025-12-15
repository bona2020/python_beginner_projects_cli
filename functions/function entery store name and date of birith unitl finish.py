def salut(name, year_of_birth):
    print(f'hello, {name} you are {age} years old & you born in {year_of_birth} ')
    print('##########################')
new_data = 'y'
while new_data != 'n':
    name = input('What is your name? ')   
    year_of_birth = int(input('Please year of birth:  '))
    age = 2025 - year_of_birth
    salut(name, year_of_birth)
    new_data = input('Would you like to make an entry? Y/N ').lower()
print('Thank you, Your data will be stored save and when you need it you can colected from our place.')

