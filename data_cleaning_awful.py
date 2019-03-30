import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
#line[0] = "Var1,Var66"

f.close()

p = open(sys.argv[2], 'w')
p.write('Var1,Var66\n')
for line in lines[1:]:
	p.write(line + '\n')

p.close()	
