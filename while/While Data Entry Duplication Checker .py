#Data Entry Duplication Checker 
result =[]
repeat = []
nrepeat = 0
while len(result)5
    something = input('Write something ')
    if not something
        print('Cant be empty..')
    elif something in result
        print('Duplicated Value. Try again')
        repeat +=something
        nrepeat +=1
    else
        result.append(something)
        print (f'[{something}] Added')
print('='40)
print(result)
print(f'These values Were entered  {nrepeat} more Time the value =  [{repeat}]')


