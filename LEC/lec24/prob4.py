
f_list = [ 19.4, 45.8, 25.2, -16, 82.19, 63.6, 45.1 ]
c_list = [(x-32)/1.8 for x in f_list if (x-32)/1.8>0 ]
line = ''
for c in c_list:
    line += '{:.2f}'.format(c) + ' '
print(line.strip())
