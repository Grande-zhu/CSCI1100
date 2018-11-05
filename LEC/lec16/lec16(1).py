imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
        
names = sorted(counts)
#limit = min(100, len(names))
max_num = 0
max_name =""
count_1 =0
for index in range(len(names)):
    name = names[index]
    if counts[name]> max_num:
        max_num = counts[name]
        max_name = name
    if counts[name] ==1:
        count_1 = count_1+1
    #print("{} appeared in {} movies".format(name, counts[name])) 
        
print("{}  appears most often: {} times".format(max_name, max_num))
print("{}  people appear once".format(count_1))
