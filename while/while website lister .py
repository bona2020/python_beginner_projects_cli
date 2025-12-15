favweb = []
a =int(input('How many website you want to list? '))
while a>0:
    web=input('enter website please: ')
    favweb.append(f'https://{web}')
    a -=1
print(favweb)
print('='*40)
a = 0
while a < len(favweb):
    favweb.sort()
    print(f'#{str(a+1).zfill(2)} {favweb[a]}')
    a +=1
print('='*40)