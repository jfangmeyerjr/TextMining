f = open('/Users/JamesFangmeyerJr/Desktop/dominican1.txt', 'r')
f.seek(0)
domdoc = f.read()
domlines = domdoc.splitlines()
# print(domlines[0].find("Dom"))
linelist = []
for line in domlines:
    if line.find('God') != -1:
        linelist.append(line)
# print(linelist)
# print(linelist.count("God")) # returns 0
print(domdoc.count("God")) # returns 40
# print(domlines.count("God")) # returns 0
print(len(linelist)) # returns 37, therefor "God" is repeated twice in 3 lines
print(len(domlines))
