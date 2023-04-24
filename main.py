import random
rand1 = int(input('From:'))
rand2 = int(input('To:'))


print("Hi! Let's play a game.\nI choose a number from", rand1, 'to', rand2, "you guess it. ")
score = 0
i = 0

while i < 10:    
    x = random.randint(rand1,rand2)

    Num1 = int(input('print your number: '))
    Num2 = x

    if Num1 == Num2:
        score = score + 1
        i = i + 1
        print('Right! \nmaybe you wanna play again?')
        
    else:
        print('Wrong answer... \nGame over\n','(Rigt answer be:',x,')')

    print(score)

    if score == 10:
        print('You win')
    else:
        None