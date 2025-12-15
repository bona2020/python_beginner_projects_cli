#Function recursive input collector that asks the user to enter 5 unique values
def enter(n,i=5):
    print(f"Enter [{i if i > 1 else 'Last'}] Entries")
    if len(n)==5:
        return n
    text=input('Write anything: ')
    if not text:
        print('Cant be empty...')
        return enter(n,i)
    elif text in n:
        print('Duplicated Value')
        return enter(n,i)
    else:
        n.append(text)
        return enter(n,i-1)
result=[]
print(enter(result))