from collections import deque


with open("input.txt", encoding="utf-8") as inp:
	ls = []
	last_ls = deque(maxlen=100)
	for i, l in enumerate(inp):
		if i <= 99: ls.append(l)
		last_ls.append(l)
	ls += last_ls
	del last_ls


with open("output.txt", 'w', encoding="utf-8") as o:
	o.writelines(ls)
