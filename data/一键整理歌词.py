import os,json
import re


file = os.listdir('歌曲')

list = []

for songs in file:
    with open(f'歌曲/{songs}', 'r+', encoding='utf-8') as f:
        songs1 = f.read()
        #songs1 = re.sub(' ', '', songs1)
        songs1 = re.sub('\n', '/', songs1)
        songs1 = re.sub('\r', '/', songs1)
        songs1 = re.sub('///', '/', songs1)
        songs1 = re.sub('//', '/', songs1)
        f.seek(0)  # 指向文本开头
        f.truncate()  # 清空文本
        f.write(songs1)
    list.append(songs1)
    print('已处理：',songs)

lyrics = str()

for songs1 in list:
    lyrics = lyrics + songs1 + '\n'

with open(f'已完成/lyrics.txt', 'w+', encoding='utf-8') as f:
    f.write(lyrics)
    print('已完成')
