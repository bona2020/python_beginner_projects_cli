#Duplicated Entery check
result=[]
def check(n,dup=[],count=0):
    if len(n)==5:
        print('='*40)
        return f'the List is:{n}\n{'='*40}\n"[{count}]" times Duplicated values enter:{dup}'
    something = input('Write something please: ')
    if not something:
        print('Cant be empty...')
        return check(n,dup,count)
    elif something in n:
        print(f'Duplicated value."[{something}]" Already Exist Try again')
        dup.append(something)
        return check(n,dup,count+1)
    else:
        n.append(something)
        print(f'"[{something}]" Added')
        return check(n,dup,count)
print(check(result))