with open('input') as f:
    line = f.readline()
line.strip('\n')
for i in range(len(line) - 3):
	if len(set(line[i:i+4])) == 4:
		print('part 1:')
		print(i + 4)
		break
for i in range(len(line) - 13):
	if len(set(line[i:i+14])) == 14:
		print('part 2:')
		print(i + 14)
		break