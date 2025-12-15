myF={}
for n in range(6):
    order = input('Write the order: ')
    name = input('Write the Name: ')
    job = input('Write the Job: ')
    myF[order]={f'Name':name,'Job':job}
else:
    print(myF)