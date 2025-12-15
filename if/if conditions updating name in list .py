family = ['Ali','Ayan','Issa','Sarah','Mohamed']
name = input('What is your name? ') .strip() .capitalize()
if name in family :
    print(f'Welcome \'{name}\' good to see you again \nyou are in the family Group list as "{name}"')
    option = input('Do you want to Update or Delete your name or No?  ') .strip() .capitalize()
    if option == 'Update' or option =='U':
        new_name= input('Please insert your name? ') .strip() .capitalize()
        family[family.index(name)] = new_name
        print(f'Your name has been updated \'{name}\' to \'{new_name}\' please check the list of family member Group below!')
        print(family)
    elif option =='Delete' or option =='D':
        family.remove(name)
        print(f'Your name has been removed \'{name}\' from the family member group list below!')
        print(family)
    elif option == 'No' or option =='N':
        print(f'No update or Delete has been done to your name \'{name}\' here is list of the family member group below! ')
        print(family)
    else:
        print(f'worng option \'{name}\' please choose Update/Delete/No')
else:
    print(f'Sorry you are not a family member\'{name}\'')
    add= input('Do you want to be added? Y/N ') .strip() .capitalize()
    if add == 'Yes' or add =='Y':
        family.append(name)
        print(f'Your name has been added \'{name}\'')
        print(family)
    else:
        print(f'Your name has not been added to the list \'{name}\'')
        print(family)