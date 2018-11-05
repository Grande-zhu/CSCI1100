filename=input("Data file name: ")
print(filename)
prefix=input("Prefix: ")
print(prefix)
len_p=len(prefix)

name_list = set()
name_p_list = set()
for line in open(filename):
    words = line.strip().split('|')
    name = words[0].strip()
    name_1 = name.split(",")
    #print(name_1[1])
    name_list.add(name_1[0])


    if name[0:len_p]==prefix:
        #print(name)
        name_p_list.add(name_1[0])
        

print(len(name_list),"last names")

print(len(name_p_list),"start with",prefix)