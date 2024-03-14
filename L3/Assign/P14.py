ab = float(input("Fuel density (in kg/L): "))
cd = float(input("Calorific value (in MJ/kg): "))
ener_mjL = ab * cd
ener_bbl = ener_mjL * 158.987

print("This fuel has energy per volume of %.2f MJ/L."%ener_mjL)
print("That is %.2f MJ/bbl."%ener_bbl)