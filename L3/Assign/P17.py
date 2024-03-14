r = float(input("ratio: "))
s = float(input("sensitivity: "))
year = 0

while True:
    if r >= s:
        print("Year %d: ratio = %s"%(year,r))
        year += 5730
        r /= 2 
        if year == 0:
            pass
    elif s >= r:
        break


        
