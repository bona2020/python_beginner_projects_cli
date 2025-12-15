# While Data Entry Checker:
result =[]
def check (tries = 5):
    if tries == 0:
        return f' All the Data Has been Entered Successfully :{result }'
    a = input('Write anything: ').strip()
    if not a :
        print('Cant be Empty...')
    elif a in result:
        print(f'Duplicated Value "{a}" Already Exist')
    else:
        result.append(a)
        print(f'"{a}" New Value Entered')
        tries-=1
    return check(tries)
print(check())