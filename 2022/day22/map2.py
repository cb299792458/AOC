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
			new_dir_idx = self.dir_idx
			(dr,dc) = self.dirs[self.dir_idx]

            # get new pos
			(row,col) = (self.row+dr,self.col+dc)
            
			# part 2 wrap (hardcoded T_T)
			if 50<col<101 and row==0:
				row=150+col-50
				col=1
				new_dir_idx=0

			if 100<col<151 and row==0:
				col=col-100
				row=200
				new_dir_idx=3
			
			if col==151 and 0<row<51:
				row=151-row
				col=100
				new_dir_idx=2

			if 100<col<151 and row==51:
				row=50+col-100
				col=100
				new_dir_idx=2

			if col==101 and 50<row<101:
				col=50+row
				row=50
				new_dir_idx=3

			if col==101 and 100<row<151:
				row=51-(row-100)
				col=150
				new_dir_idx=2

			if 50<col<101 and row==151:
				row=150+col-50
				col=50
				new_dir_idx=2

			if col==51 and 150<row<201:
				col=50+row-150
				row=150
				new_dir_idx=3
			
			if 0<col<51 and row==201:
				col=col+100
				row=1
				# new_dir_idx=2

			if col==0 and 150<row<201:
				col=50+row-150
				row=1
				new_dir_idx=1

			if col==0 and 100<row<151:
				row=151-row
				col=51
				new_dir_idx=0

			if 0<col<51 and row==100:
				row=50+col
				col=51
				new_dir_idx=0

			if col==50 and 50<row<101:
				col=row-50
				row=101
				new_dir_idx=1

			if col==50 and 0<row<51:
				row=151-row
				col=1
				new_dir_idx=0

            # check for blocked path
			if map[row][col]=='#': return

            # move to new spot
			(self.row,self.col) = (row,col)
			self.dir_idx = new_dir_idx
			self.draw()

	def draw(self):
	    map[self.row][self.col] = 'X'


# w = Walker()
# # print(len(map))

# w.row = 3
# w.col = 53
# w.draw()
# w.turn('R')
# w.turn('R')
# w.walk(15)

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