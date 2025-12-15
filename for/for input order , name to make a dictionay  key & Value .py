myF={}
for n in range (6):
    order = input('Write the order: ')
    name = input('Write the Name: ')
    myF.update({order:name})
else:
    print(myF)