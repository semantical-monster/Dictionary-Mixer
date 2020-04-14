file  = open('file.txt','r').readlines()
x = []

for start in file:
	x.append(start.strip('\n'))

def mix(c, b):
	if c in each:
		x.append(each.replace(c,b))
		x.append(each.replace(c,b,1))
		x.append(each.replace(c,b,2))
		re = each[::-1]
		abc = re.replace(c,b)
		x.append(abc[::-1])
		abc = re.replace(c,b,1)
		x.append(abc[::-1])
		abc = re.replace(c,b,2)
		x.append(abc[::-1])


mixes = {'o': '0', 'e':'3', 'l':'1', 'i':'1', 'a':'@', 's':'$'}

for k, v in mixes.items():
	for each in set(x):
		mix(k,v)

print(set(x))
print(len(set(x)))
print("unique values generated from orignal")
print(len(file))


new = open('new.txt','r+')
for yo in set(x):
	new.write(yo + '\n')




