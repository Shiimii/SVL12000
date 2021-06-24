import random

level = input("level: ")

with open('Level{0:0>2}.txt'.format(level), 'r', encoding='UTF-8', newline='\n') as file:
    data = file.readlines()

rand = random.randint(0,999)
print(data[rand].rstrip('\n'))

