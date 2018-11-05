line = ""
for i in range(9):
    line = line + str(i)+" "
print(line)

line1="0"
for i in range(1,9):
    line1+=" "+str(i)
print(line1)

line = ""
i =0
while i < 9:
    line = line + str(i)+" "
    i = i+1
print(line)    

print()
for i in range(9):
    line=""
    for j in range(9):
        line = line + str(i) + "," + str(j) + " "
    print(line)


i=0
while i<7:
    print()
    for k in range(i,i+3):
        line=""
        j=0
        while j<7:
            for w in range(j,j+3):
                line=line+str(k)+","+str(w)+" "
            line = line + " "
            j = j+3
        print(line)
    i = i+3
    
print()

for i in range(3):
    line=""
    for j in range(3):
        line = line + str(i) + "," + str(j) + " "
    print(line)
