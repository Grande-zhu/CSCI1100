file_name_1 = input("Enter the scores file: ")
print(file_name_1)
file_name_1 = open(file_name_1)


line=[]
while True:
    line1 = file_name_1.readline()
    line1 = line1.strip()
    #print(line1)
    if line1:
        line.append(line1)
    else:
        break

line = sorted(line,key = int)
#print(line)



file_name_2= input("Enter the output file: ")
print(file_name_2)
f_out = open(file_name_2,"w")

for i in range(len(line)):
    if int(line[i])>99:
        f_out.write("{:d}:    {:3d}\n".format(i,int(line[i])))
    else:
        f_out.write("{:d}:    {:2d}\n".format(i,int(line[i])))
open(file_name_2)
