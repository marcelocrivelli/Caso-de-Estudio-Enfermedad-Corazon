fileName = "switzerland"

f = open(fileName + '.data', "r", errors='ignore')

lines = 9
data = []
row = ""
for line in f:
	splt = line.split(' ')
	for s in splt:
		if '\n' in s:
			s = s.replace('\n','')
		row += s + ' '
	if lines > 0:
		lines -= 1
	else:
		# Sin el espacio final
		data.append(row[:-1])
		row = ""
		lines = 9

f.close()
# print(data)

out = open(fileName + "final.data", "w")

for i in data:
	out.write(i + '\n')

print(len(data))

out.close()
