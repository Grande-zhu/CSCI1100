
points = [ (4,2), (1,-3), (-4, -6), (4,9), (-7,8), (-5,2), (6,2) ]
s_points = sorted( points, key = lambda p: (p[0]**2+p[1]**2), reverse=True )
print(s_points)
