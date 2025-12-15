people = {}
for n in range(3):
    name = input('Write The Name Please: ').strip().title()
    people[name]={}
    for n in range(3):
        skill = input('Write a Skill please: ').strip().title()
        level = input('Write The Level Please: ').strip()
        people[name][skill] = level
        people[name][skill] = f'{level}%'
else:
    print(people)
    print('='*40)
for name in people:
    print(f'the Skills for "{name}" are: ')
    print('#'*40)
    for skill in people[name]:
        print(f'-{skill} => {people[name][skill]}')