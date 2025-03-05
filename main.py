import random


def game():
    secret_number = random.randint(1, 100)
    attempts = 0 
    score = 0
    
    
    while True:
        
        print('Please select the difficulty level: \n 1. Easy (10 chances) \n 2. Medium (5 chances) \n 3. Hard (3 chances)')
        choices = input('enter yor choisec: ')

        if choices == '1':
            while score < 10:
                try:
                    usr = int(input('enter your value:'))
                except ValueError:
                    print('введите целое число')
                    continue
                score += 1 
                attempts += 1
                
                if score < 10:
                    if usr < secret_number:
                        print('загаданное число больше')
                    elif usr > secret_number:
                        print('загаданное число меньше')
                    else:
                        print(f'вы угадали число {secret_number} за {attempts} попыток')
                        break
                else:
                    print('you luse :(')
                    break
                    
            
        
        elif choices == '2':
            while score < 5:
                try:
                    usr = int(input('enter your value:'))
                except ValueError:
                    print('введите целое число')
                    continue
                score += 1 
                attempts += 1
                
                if score < 5:
                    if usr < secret_number:
                        print('загаданное число больше')
                    elif usr > secret_number:
                        print('загаданное число меньше')
                    else:
                        print(f'вы угадали число {secret_number} за {attempts} попыток')
                        break
                else:
                    print('you luse :(')
                    break
            
            
        elif choices == '3':
            while score < 3:
                try:
                    usr = int(input('enter your value:'))
                except ValueError:
                    print('введите целое число')
                    continue
                score += 1 
                attempts += 1
                
                if score < 3:
                    if usr < secret_number:
                        print('загаданное число больше')
                    elif usr > secret_number:
                        print('загаданное число меньше')
                    else:
                        print(f'вы угадали число {secret_number} за {attempts} попыток')
                        break
                else:
                    print('you luse :(')
                    break
            
        
game()