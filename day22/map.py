input = open('input.txt','r').readlines()
input = [a[:-1] for a in input]

# parse input to make map and path
map = [[]] + [ [' '] + [char for char in line] for line in input[0:-2]]
instructions = input[-1]
path=[]
temp=''
for char in instructions:
	if char=='R' or char=='L':
		if temp: path.append(int(temp))
		path.append(char)
		temp=''
	else: temp+=char
path.append(int(temp))

# make ranges for wrap
row_ranges = [None]
col_ranges = [None]
for i in range(1, len(map)):
	c = 1
	while map[i][c]==' ': c+=1
	low=c
	col_ranges.append((low,len(map[i])-1))
for i in range(1,max( [len(row) for row in map ] )):
	r = 1
	while i>=len(map[r]) or map[r][i] == ' ': r+=1
	low = r
	while r<len(map) and i<len(map[r]) and map[r][i] != ' ': r+=1
	high = r
	row_ranges.append((low,high-1))
# print(col_ranges)
# print(row_ranges)



class Walker:
	    
	def __init__(self):
		self.dirs = [(0,1),(1,0),(0,-1),(-1,0)]
		self.row = 1
		self.col = 1
		while map[self.row][self.col]==' ':
			self.col += 1
		self.dir_idx = 0

	def turn(self,RorL):
		if RorL=='R': self.dir_idx = (self.dir_idx+1)%4
		elif RorL=='L': self.dir_idx = (self.dir_idx-1)%4

	def walk(self,steps):
		for _ in range(steps):
			(dr,dc) = self.dirs[self.dir_idx]

			# get new pos
			(row,col) = (self.row+dr,self.col+dc)

			# wrap
			# print(row)
			if dc==-1 and col<col_ranges[row][0]: col = col_ranges[row][1]
			if dc==1 and col>col_ranges[row][1]: col = col_ranges[row][0]
			if dr==-1 and row<row_ranges[col][0]: row = row_ranges[col][1]
			if dr==1 and row>row_ranges[col][1]: row = row_ranges[col][0]	
			



			# check for blocked path
			if map[row][col]=='#': return

			# move to new spot
			(self.row,self.col) = (row,col)

	def draw(self):
	    map[self.row][self.col] = 'X'


# w = Walker()

# w.row = 6
# w.col = 3
# w.turn('L')
# w.walk(3)

# w.draw()

v = Walker()
for step in path:
	if step=='L' or step=='R':
		v.turn(step)
	else:
		v.walk(step)
v.draw()
print( 1000*v.row + 4*v.col + v.dir_idx )


# print map to txt
file = open('output.txt','w')
for line in map:
	if line: file.write(''.join(line)+"\n")
file.close()