def martian_botanist(number, daily, produc):
    total = number * daily
    area = total / produc
    return area
    




if __name__ == "__main__":
    area = martian_botanist(150, 2, 2.4)
    print('planting area:', area, 'sq. m.')
    area = martian_botanist(900, 2.5, 1.2)
    print('planting area:', area, 'sq. m.')
    area = martian_botanist(200, 2.4, 1.6)
    print('planting area:', area, 'sq. m.')