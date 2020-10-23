import random

def randomize(text):
    l = list(text)
    for i in range(len(l)):
        roll = random.randint(0, 1)
        if l[i].isalpha():
            if l[i] == 'l':
                l[i] = l[i].upper()
                continue
            if roll == 0:
                l[i] = l[i].upper()
    return ''.join(l)

for i in range(50):
    print(randomize('hello world'))