import math
def get_response_time(beach):
    d_1 = beach[0]
    d_2 = beach[1]
    h = beach[2]
    vsand = beach[3]
    n = beach[4]
    theta1 = beach[5]
    
    d_1 = float(d_1)*3
    d_2 = float(d_2)
    h = float(h)*3
    vsand = float(vsand)*5280/3600
    vswim = vsand/float(n)
    x = math.tan(float(theta1)/180*math.pi)*d_1
    n = float(n)
    theta1 = int(round(float(theta1),0))
    
    L1 = math.sqrt(x**2+d_1**2)
    L2 = math.sqrt((h-x)**2+d_2**2)
    t = 1/vsand*(L1+n*L2)    
    return t