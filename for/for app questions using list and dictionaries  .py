# 1. Outcome - score
# 2. Income  - Question, correct option, marks, user choices
score = 0
failed = 0
q_failed =[]
 
questions = [{
    "question": "1.What is the capital of USA?",
    "options": ['1)Washington dc', '2)Hyderabad', '3)Hongkong'],
    "correct": 1
}, 
{
    "question": "2.Corona virus scientific name?",
    "options": ['1)Flue', '2)Covid19', '3)Fever'],
    "correct": 2
},
{
    "question": "3.What is the easiest programming language?",
    "options": ['1)Java', '2)Python', '3)C++'],
    "correct": 2
},
{
    "question": "4.What is the the Use of python language?",
    "options": ['1)Ai', '2)Maching learning', '3)App building','4)All of above'],
    "correct": 4
}
]
 
for i in questions:
    print(i['question'])
    for v in i['options']:
        print(v)
    print('-'* 8)
    ans = input('Enter your answer: ')   
    print('-'* 8)
    if int(ans) == i['correct']:
        score += 1
    else:
        failed +=1
        q_failed.append(i['question'])
print(f'Congrats Your score is: {score}/4'if score >1 else f'Please! Try again later your score is {score}/4 ')
print('='*44)
if failed > 0:
    print(f'Number of failed questions {failed} -> failed questions are :')
    for j in q_failed:
        print(j)