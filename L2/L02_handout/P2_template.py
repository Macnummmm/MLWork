"""
Given a reaction of burning gas methane (CH4) in air: 
CH4 + 2 O2 --> CO2 + 2 H2O and the fact that 
when either CH4 or O2 runs out first the reaction stops and the other is left over. 
Write a function, named "ch4combus", to take in weights (in gram) of  CH4 and O2 and 
reports what will be left after the burning.
Note: 
    molar mass M = mass (in kg) of 1 mole of the substance;
    1 mole = 6.02214076×10^23 particles (e.g., molecules, atoms, ions, electrons, etc.).
    molar mass of water = 18.015 g/mol
    atomic weight: 
        H ~ 1.008 g/mol; C ~ 12.011 g/mol; O ~ 15.999 g/mol
	https://en.wikibooks.org/wiki/General_Chemistry/Energy_changes_in_chemical_reactions
"""

# Write your function here

    # (1) find molecular weights (in g/mol)
	# e.g., CH4 weighs 12.011 + 1.008*4 (g/mol)


    # (2) find numbers of moles of methane and oxygen, 
    # e.g., # CH4 moles = (methane in g)/(CH4 weight in g/mol);

    # (3) compare (# CH4 moles) to (# O2 moles / 2); 
    # e.g., 3 CH4 moles matches to 6 O2 moles.

    # if CH4 is larger, the CH4 excess will be left 
	# and O2 will be used up;
    # and vice versa.
    # (4) The combined product weight =  methane_g + oxygen_g - the excess

    # (5) work out the product proportion to find CO2 and H2O weights,
    # e.g., total CO2 weight/total product weight = CO2 / (CO2 + 2 H2O).

# Do not edit below this line.
# ==============================================================
	
if __name__ == '__main__':
    m = input('Methane (CH4, in g):')
    o = input('Oxygen (O2, in g):')
    print('CH4: %.2f g. O2 %.2f g. CO2 %.2f g. H2O %.2f g'%
        ch4combus(float(m), float(o)))

