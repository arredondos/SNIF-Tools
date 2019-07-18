from sys import argv
from csv import writer

def chunks(arr, n):
	for i in range(0, len(arr), n):
		yield arr[i : i + n]

filename = argv[1]
lines = [line.rstrip('\n') for line in open(filename)]#, encoding='utf-16')]

k = int(lines[0].split()[1])
blocks = [chunk[4:] for chunk in chunks(lines[2:], k + 4)]

afs = [0] * (k - 1)
for b in blocks:
	l = len(b[0])
	for j in range(l):
		snp_id = sum(int(b[i][j]) for i in range(k))
		afs[snp_id - 1] += 1	

total = sum(afs)
normalized_afs = [xi / total for xi in afs]

outfilename = filename + '-afs.csv'
writer(open(outfilename, 'w', newline='')).writerows([normalized_afs])