file=open("1.py","r")
condition=["if","elif","while","for","switch"]
count=1
for i in file:
    c=10000;
    if "#" in i:
        if i.find("#")==0:
            continue
        else:
            c=i.find("#")

    for j in condition:
        if j in i and ':' in i and i.find(j)<c:
            count+=1
print "Cyclometric complexity is : "+str(count)
