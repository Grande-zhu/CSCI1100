def find_min(List):
    min_value = List[0][0]
    for i in range(len(List)):
        for r in range(len(List[i])):
                  
            if (List[i][r])< (min_value):
                min_value = List[i][r]
        
    return min_value

if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ],
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )