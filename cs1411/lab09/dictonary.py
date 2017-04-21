file_temp = open('togive.txt','r')
new = {}
for line in file_temp:

	line = line.split()

	new[line[0]]= [line[i] for i in range(2, 7)]

print(new)
