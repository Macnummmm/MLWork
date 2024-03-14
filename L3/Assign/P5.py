def mighty_river(rivers):

    P_kinetic = {}
    # Write your code here
    for key, val in rivers.items():
        x = val[0]
        rho = val[1]
        y = val[2]
        total = 0.5 * rho * y**3 / x**2
        P_kinetic[key] = total

    return P_kinetic

if __name__ == '__main__':
                # name  : [A (m^2), rho (kg/m^3),  Q (m^3/s)]
    mighties = {'Amazon': [1.2e6, 1100, 210000],
                'Congo':  [2e6, 1150, 41200],
                'Yangtze': [800e3, 1200, 30000]}

    river_power = mighty_river(mighties)
    print(river_power)
