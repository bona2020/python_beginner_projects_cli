def greetings_ms():
    print('Hello, Ms. ' + name +   ' how are you ' )
def greetings_mr():
    print('Hello, Mr. ' + name +   ' how are you ' )
def greetings_mrs():
    print('Hello, Mrs. ' + name +   ' how are you ' )


name = input('Please give your name: ')
gender = input('What is your pronounce? M/F ') .lower()

if gender == 'f':
    is_married = input('Are you married? ')
    if is_married == 'y':
        greetings_mrs()
    else:
        greetings_ms()
else :
    greetings_mr()
