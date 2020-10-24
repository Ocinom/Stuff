import random

task = [i for i in range(10)]
random.shuffle(task)

for i in range(5):
    print([task[2*i], task[2*i + 1]])
