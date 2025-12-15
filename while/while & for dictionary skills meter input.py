# a = {'Html':'50%','Css':'60%','PHP':'30%','Python':'90%'}
a={}

while len(a) < 5:
    print(type(a))
    b = input('what are you skills ? ') .strip() .capitalize()
    c = input('What is your progress in this skills ').strip()
    a.update({b:c+'%'})
print('='*50)
print(a)
print('='*50)

for i in a :
    print(f'Your skills are {i} and your progress are {a[i]}')