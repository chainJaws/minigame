import random


def game():
    secret_number = random.randint(1, 100)
    attempts = 0 
    
    while True:
        try:
            usr = int(input('enter your value:'))
        except ValueError:
            print('введите целое число')
            continue
        
        attempts += 1
        
        if usr < secret_number:
            print('загаданное число больше')
        elif usr > secret_number:
            print('загаданное число меньше')
        else:
            print(f'вы угадали число {secret_number} за {attempts} попыток')
            break
        
game()