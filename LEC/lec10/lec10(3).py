co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ] 
avg = sum(co2_levels)/len(co2_levels)
print ("Average: {:.2f}".format(avg))
num = 0
for co2_level in co2_levels:
    if co2_level >avg:
        num = num+1
print("Num above average:",num)
