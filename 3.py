adjacency_mat = {}
stack = []

lines = []
f = open('c.txt','r')
lines = f.readlines()


nodeCount=0
for i in range(0, len(lines)):
    if("{" in lines[i]):
        if("()" in lines[i]):
            nodeCount+=1
            adjacency_mat[i]=[i+1]
            continue
        if("if" in lines[i]):
            stack.append([1,i])            
            nodeCount+=1
            adjacency_mat[i]=[i+1]
            continue
        if("for" in lines[i]):
            stack.append([2,i])            
            nodeCount+=1
            adjacency_mat[i]=[i+1]
            continue
    if("}" in lines[i]):
        if(len(stack)>0):
            arr = stack.pop()
            type=arr[0]
            line=arr[1]
            if(type==1):
                nodeCount+=1
                adjacency_mat[i]=[i+1]
                adjacency_mat[line].append(i+1)
                continue
            if(type==2):
                nodeCount+=1
                adjacency_mat[i]=[line]
                adjacency_mat[line].append(i+1)
                continue
        else:
            adjacency_mat[i]=[]
            nodeCount+=1
            continue
    nodeCount+=1
    adjacency_mat[i]=[i+1]

edgeCount=0 
#
#print(" THE FLOW GRAPH IS : ")
for i in adjacency_mat.keys():
    #print(i," -> ",end='')
    for n in adjacency_mat[i]:
        edgeCount+=1
        #print(n,end='\t')
    #print("")
print "NodeCount : ",nodeCount
print "EdgeCount : ",edgeCount
print "Cyclomatic Complexity = EdgeCount-NodeCount+2 = ",edgeCount-nodeCount+2