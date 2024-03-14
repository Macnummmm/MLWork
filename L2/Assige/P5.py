
def numsys (to):
    b = bin(to)
    h = hex(to)
    return b, h

if __name__ == "__main__":

    results = numsys (20)
    print('results = ', results)
    
    b, h = numsys (30)
    print('b = ', b)
    print('h = ', h)
