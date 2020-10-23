from random import choice as c

prompt = input('You playing or nah(y/n)\n')

while prompt != 'y' and prompt != 'n':
    prompt = input('y or n you daft animal\n')
else:
    if prompt == 'n':
        exit()

res = {
    'r' : 'p',
    'p' : 's',
    's' : 'r'
}
ch = ['r', 'p', 's']

game = input("Choose r for rock, p for paper, s for scissors\n")

while game not in ch:
    game = input('nice try. r, p, or s only.')

v = c(ch)
print('CPU chose ' + v)
if res[v] == game:
    print('LOSE')
elif res[game] == v:
    print('WIN')
else:
    print('DRAW')
