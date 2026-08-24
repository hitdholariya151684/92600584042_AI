print('='*30)
print('GUESS NUMBER SYSTEM')
print('='*30)
print('Guess a number between 1 to 100')
print('If my guess is correct, press C.')
print('If my guess is too High, press H.')
print('If my guess is too Low, press L.\n')
l = 1
h = 100
while l <= h:
    a = (l + h) // 2
    print('Is your number',a,'?')
    n = input('Your choice from (C/H/L): ').lower()
    if n == 'c':
        print('\nWow! I guessed your number:',a)
    elif n == 'h':
        h = a - 1
    elif n == 'l':
        
        l = a + 1
    else:
        print('Invalid input! Please enter from this C, H, or L.')
else:
    print("\nSomething went wrong.")
