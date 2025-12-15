people ={}
n = 3
while n > 0:
    name = input('Write the Name please: ').title().strip()
    people[name]={}
    n -=1
    s = 3
    while s >0:
        skill=input('Write a skill please: ').strip().upper()
        level = input('Write the Level: ').strip()
        experience=input('Write the Experience: ').strip()
        # people[name][skill]={level:experience}
        # people[name][skill]={'Level':level,'Experience':experience}
        people[name]={'Skill':skill,'Level':f'{level} %','Experience':f'{experience} Years'}
        s-=1
else:
    print(people)


    