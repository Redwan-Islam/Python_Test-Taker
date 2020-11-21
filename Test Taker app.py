
print('Welcome To Test Taker! , Developed By Redwan')
print(' ## GIVE ANSWER IN LOWERCASE ##')
play = input('Are you ready to play(yes/No):  ')
score = 0
total_question = 5

if play.lower() == 'yes':
    play = input('1. which programing language i used to make this Test Taker app? ')
    if play.lower() == 'python':
        score += 1
        print('correct')
    else:
        print('incorrect. you are so close try again.')

    play = input('2. What is the capital of Bangladesh? ')
    if play.lower() == 'dhaka':
        score +=1
        print('correct')
    else:
        print('incorrect. you are so close try again.')

    play = input('3. what is 2+2-1+3*0-1+2+3? ')
    if play.lower() == '0':
        score +=1
        print('correct')
    else:
        print('incorrect. you are so close try again.')

    play = input('4. Who is the developer of this Test Taker app? ')
    if play.lower() == 'redwan':
        score +=1
        print('correct')
    else:
        print('incorrect. you are so close try again.')

    play = input('5. How many bones in Human body? ')
    if play.lower() == '206':
        score +=1
        print('correct')
    else:
        print('incorrect. you are so close try again.')

print('Thank you for playing Test Taker, you got',score,"Question qurrect. ")
mark = (score/total_question) * 100

print('mark: ', mark)
print('Good Bye')

    
