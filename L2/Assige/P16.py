"""
Saffir–Simpson scale assign category to a storm
according to wind speed:
>= 252 km/h as Category 5, 209-251 km/h as Category 4,
178-208 km/h as Category 3, 155-177 km/h as Category 2,
119-153 km/h as Category 1.
Also, storm with wind speed 63-118 km/h is classified
as Tropical Storm and one with wind speed <= 62 km/h
is classified as Tropical Depression.

Write a function named typhoon to take in 4 arguments:
wind speed (in Km/h), air density (in Kg/m3),
effective area (in Km2), and effective height (in m),
find its category and estimated energy,
return a list of category name and estimated energy.
"""


def typhoon(wspeed, adensity, area, height):
    storm_scale = [
        ["Category 5", 252],
        ["Category 4", 209],
        ["Category 3", 178],
        ["Category 2", 155],
        ["Category 1", 119],
        ["Tropical Storm", 63],
        ["Tropical Depression", 0],
    ]

    # Find storm type
    storm = ""
    for category, threshold in storm_scale:
        if wspeed >= threshold:
            storm = category
            break
    # Write your code here

    # wind velocity in m/s
    v = wspeed / 3.6  # dummy
    # Write your code here

    # air density in Kg/cu. m
    rho = adensity  # dummy
    # Write your code here

    # Area in sq. m
    A = area * 1e6  # dummy
    # Write your code here

    # Height in m
    H = height  # dummy
    # Write your code here

    # air mass in Kg
    m = rho * A * H  # dummy
    # Write your code here

    E = 0.5 * m * v**2

    return [storm, E]


if __name__ == "__main__":
    for v in range(0, 280, 10):
        res = typhoon(v, 1.225, 80424, 15240)
        # rho = 1.225 kg/cu. m
        # A = diameter 160 km ~ 80424 sq km
        # H = 50000 ft = 15240m
        print("%d km/h:" % v, "{} Energy {:,.5} J".format(res[0], res[1]))
