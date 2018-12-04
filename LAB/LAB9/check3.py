from Date import *
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]
fname="birthdays.txt"
line1=[]
for lines in open(fname):
    line = lines.strip('\n')
    line = line.split(' ')
    date = Date(int(line[0]),int(line[1]),int(line[2]))
    line1.append(date)
    
earliest_birthday=Date(2800,12,31)
latest_birthday=Date()

for i in range (len(line1)):
    if line1[i]<earliest_birthday:
        earliest_birthday = line1[i]
print("earliest_birthday",earliest_birthday)

for i in range (len(line1)):
    if latest_birthday<line1[i]:
        latest_birthday = line1[i]
print("latest_birthday",latest_birthday)

Birthday=dict()
Birthday[month_names[1]]=0
Birthday[month_names[2]]=0
Birthday[month_names[3]]=0
Birthday[month_names[4]]=0
Birthday[month_names[5]]=0
Birthday[month_names[6]]=0
Birthday[month_names[7]]=0
Birthday[month_names[8]]=0
Birthday[month_names[9]]=0
Birthday[month_names[10]]=0
Birthday[month_names[11]]=0
Birthday[month_names[12]]=0

for i in range (len(line1)):
    if line1[5:7]=="01":
        Birthday[month_names[1]] += 1
    elif line1[5:7]=="02":
        Birthday[month_names[2]] += 1
    elif line1[5:7]=="03":
        Birthday[month_names[3]] += 1
    elif line1[5:7]=="04":
        Birthday[month_names[4]] += 1
    elif line1[5:7]=="05":
        Birthday[month_names[5]] += 1
    elif line1[5:7]=="06":
        Birthday[month_names[6]] += 1
    elif line1[5:7]=="07":
        Birthday[month_names[7]] += 1
    elif line1[5:7]=="08":
        Birthday[month_names[8]] += 1
    elif line1[5:7]=="09":
        Birthday[month_names[9]] += 1
    elif line1[5:7]=="10":
        Birthday[month_names[10]] += 1
    elif line1[5:7]=="11":
        Birthday[month_names[11]] += 1
    elif line1[5:7]=="12":
        Birthday[month_names[12]] += 1   
        
max_value=max(Birthday.values())
list_key=list(Birthday.keys())
list_value=list(Birthday.values())
max_index=list_value.index(max_value)
max_month=list_key[max_index]
print(max_month,"has the most birthday")