def survive_mars(area, depth):
    volume = (area / 100) * depth 
    total = volume * 40
    return total


if __name__ == "__main__":
    w = survive_mars(126, 30)
    print('water', w, 'L')

    w = survive_mars(150, 40)
    print('water', w, 'L')

    w = survive_mars(100, 35)
    print('water', w, 'L')