w = float(input("Waste: "))
c = float(input("Cap: "))
total_w = w * (70000000)
land = (total_w / c) / 1600
annual_land = land * 365

print("Total waste= %.2f"%total_w)
print("Landfill= %.2f"%land)
print("Annual land= %.2f"%annual_land)
