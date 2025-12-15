# Data Entry Checker:
result=[]
while len(result)<10:
    a = input('Write anthing: ').strip()
    if not a:
        msg = 'Cant be Empty.....'
    elif a in result:
        msg = f'Duplicated Value "{a}"" Already Exist'
    else:
        msg = f'"{a}" New Value Added'
        result.append(a)
    print(msg)
print(f'Printing All Entered Data: {result}')