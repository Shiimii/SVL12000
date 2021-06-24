import requests
import re

def make_list(n):
    file_path = 'http://web.archive.org/web/20081219085635/http://www.alc.co.jp/goi/svl_l{0:0>2}_list.htm'.format(n)
    # print(file_path)
    # get a list
    res = requests.request('get', file_path)
    lst = res.text

    # split
    lines = lst.splitlines()

    # filter
    lines = [line for line in lines if '<br>' in line or '</font>' in line]
    lines = lines[4:1004]

    # remove 
    lines = [line.replace(' ', '') for line in lines]
    ptn = re.compile(r"<[^>]*?>")
    lines = [ptn.sub('', line) for line in lines]

    # print(lines)
    # print(len(lines))
    return lines

def save_list(n, data):
    # to start new line
    data = [val+'\n' for val in data]
    with open('./checklist/Level{0:0>2}.md'.format(n), 'w', encoding='UTF-8', newline='\n') as file:
        file.writelines(data)

for i in range(1, 13):
    list = make_list(i)
    list = ["- [ ] "+line for line in list]
    save_list(i, list)
    # print(make_list(i))