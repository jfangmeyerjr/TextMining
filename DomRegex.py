f = open('/Users/JamesFangmeyerJr/Desktop/dominican1.txt', 'r')
f.seek(0)
domdoc = f.read()
import re
print(re.findall('Fr.\s[^0-9+ | \s]', domdoc))
