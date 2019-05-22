adjacency_mat = {}
stack = []

lines = []
f = open('c.txt','r')
lines = f.readlines()

numRegions=1
for i in range(0, len(lines)):
    if("else if" in lines[i]):
        numRegions+=1
        continue
    if("if" in lines[i]):
        numRegions+=1
        continue
    if("for" in lines[i]):
        numRegions+=1
    if("while" in lines[i]):
        numRegions+=1
print "Number of Regions = ",numRegions 
print "Hence Cyclomatic Complexity = ",numRegions 