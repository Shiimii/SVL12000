word = input("word: ")

flag = 0
for level in range(1,13):
    # print(level)
    with open('Level{0:0>2}.txt'.format(level), 'r', encoding='UTF-8', newline='\n') as file:
        data = file.readlines()
    data = [line.rstrip("\r\n") for line in data]
    if word in data:
        print(f'level: {level}')
        flag = 1
        break
if not flag:
    print("Not found")