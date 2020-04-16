file  = open('file.txt','r').readlines()
x = []

for start in file:
	x.append(start.strip('\n'))

def mix(c, b, each):

	if each.count(c) == 4:
		xyz2 = int(0)
		while xyz2 < each.count(c):
			x.append(each.replace(c,b,xyz2))
			xyz2 += 1
		
		re = each[::-1]
		xyz = int(1)
		while xyz < each.count(c):
			abc = re.replace(c,b,xyz)
			x.append(abc[::-1])
			xyz += 1

		s1 = each.split(c)
		x.append(s1[0] + c + s1[1] + c + s1[2] + b + s1[3] + c + s1[4])
		x.append(s1[0] + c + s1[1] + b + s1[2] + c + s1[3] + c + s1[4])
		x.append(s1[0] + c + s1[1] + b + s1[2] + c + s1[3] + b + s1[4])
		x.append(s1[0] + c + s1[1] + b + s1[2] + b + s1[3] + c + s1[4])
		x.append(s1[0] + b + s1[1] + c + s1[2] + c + s1[3] + b + s1[4])
		x.append(s1[0] + b + s1[1] + c + s1[2] + b + s1[3] + c + s1[4])
		x.append(s1[0] + b + s1[1] + c + s1[2] + b + s1[3] + b + s1[4])
		x.append(s1[0] + b + s1[1] + b + s1[2] + c + s1[3] + b + s1[4])

	if each.count(c) == 3:
		xyz2 = int(0)
		while xyz2 < each.count(c):
			x.append(each.replace(c,b,xyz2))
			xyz2 += 1
		
		re = each[::-1]
		xyz = int(1)
		while xyz < each.count(c):
			abc = re.replace(c,b,xyz)
			x.append(abc[::-1])
			xyz += 1

		s1 = each.split(c)
		x.append(s1[0] + b + s1[1] + c + s1[2] + b + s1[3])
		x.append(s1[0] + c + s1[1] + b + s1[2] + c + s1[3])
	
	if each.count(c) == 2:
			x.append(each.replace(c,b,1))
			x.append(each.replace(c,b,2))
			re = each[::-1]
			abc = re.replace(c,b,1)
			x.append(abc[::-1])
	
	if each.count(c) == 1:
		x.append(each.replace(c,b,1))

mixes = {'o': '0', 'e':'3', 'l':'1', 'i':'1', 'a':'@', 's':'$'}

for k, v in mixes.items():
	for item in set(x):
		mix(k,v, item)

print(x)
print(len(x))
print("unique values generated from orignal")
print(len(file))

new = open('new.txt','r+')
for yo in set(x):
	new.write(yo + '\n')