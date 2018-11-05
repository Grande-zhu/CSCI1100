def find_next(bpop,fpop):
    bpop_next = max((10*bpop)/(1+0.1*bpop)-0.05*bpop*fpop,0)
    fpop_next=max(0.4*fpop+0.02*fpop*bpop,0)    
    return(bpop_next,fpop_next)

bpop=input("Numbers of bunnies==>")
print(bpop)
fpop=input("Numbers of foxes==>")
print(fpop)
bpop=int(bpop)
fpop=int(fpop)
print("Year 1: {} {}".format(bpop,fpop))
bpop_next=find_next(bpop,fpop)[0]
fpop_next=find_next(bpop,fpop)[1]
bpop=int(bpop_next)
fpop=int(fpop_next)
print("Year 2: {} {}".format(bpop,fpop))     
bpop_next=find_next(bpop,fpop)[0]
fpop_next=find_next(bpop,fpop)[1]
bpop=int(bpop_next)
fpop=int(fpop_next)
print("Year 3: {} {}".format(bpop,fpop))     
bpop_next=find_next(bpop,fpop)[0]
fpop_next=find_next(bpop,fpop)[1]
bpop=int(bpop_next)
fpop=int(fpop_next)
print("Year 4: {} {}".format(bpop,fpop))    
bpop_next=find_next(bpop,fpop)[0]
fpop_next=find_next(bpop,fpop)[1]
bpop=int(bpop_next)
fpop=int(fpop_next)
print("Year 5: {} {}".format(bpop,fpop))    
