import random
import sys
a=int(input('Enter the starting range:'))
b=int(input('Enter the ending range: '))
if a>b:
    a,b=b,a
n=random.randint(a,b)
i=0
while i<3:
    m=int(input('Guess:'))
    i += 1
    if m>b:
        print(f"range should be less than {b}")
        sys.exit()
    elif n==m:
        print('congratulations!')
        break

else:
    print('sorry!')
print(f'Random no. is {n}')