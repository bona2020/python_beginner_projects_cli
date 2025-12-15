myF={}
for n in range(6):
    order = input('Write the order: ').title().strip()
    name = input('Write the Name: ').title().strip()
    job = input('Write the Job: ').upper().strip()
    myF[order]={name:{'Job':job}}
else:
    print(myF)