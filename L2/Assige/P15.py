def earthquake(x) :
    lst = []
    for i in x :
        ev = 10 ** ( 4.8 + (1.5 * i[1]) )
        i.append(ev)
        lst.append(i)

    return lst


if __name__ == '__main__':
    Events = [['2019 02 22 Ecuador', 7.5],
              ['2018 08 19 Fiji', 8.2],
              ['2017 09 08 Mexico', 8.2]]
    res = earthquake(Events)
    print(res)