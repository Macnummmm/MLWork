def est_prob ( cu ) :
    res = []
    s = sum(cu)
    for i in cu:
        res.append(i / s)
    return res

if __name__ == "__main__":
    counting = [0, 8, 20, 4, 12]
    res = est_prob(counting)
    print(res)