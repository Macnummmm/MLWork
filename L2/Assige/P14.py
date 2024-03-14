def laplace_smooth(cu, am):
    lst = []
    for i in cu:
        p = ( i + am ) / ( sum(cu) + (am * len(cu)) )
        lst.append(p)

    return lst


if __name__ == '__main__':
    counting = [0, 8, 20, 4, 12]
    res = laplace_smooth(counting, 0.1)

    print(res)