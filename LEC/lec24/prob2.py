
points = [ (4,2), (1,-3), (-4, -6), (6,9), (3,8), (-5,2), (6,2) ]


def first_qua(points):
        if points[0]>0 and points[1]>0:
                return points

min_x=list(map( first_qua, points))
min_x=list(filter( lambda x:x, min_x ))
min_x=list(min(min_x))[0]


print(min_x)
