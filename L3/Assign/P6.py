def rational_decision(s, p):
    ck_nc = 0
    c_c = 0
    n_c = s[p][0]
    con = s[p][1]

    for i in range(0, len(con)):
        if n_c[i] > con[i]:
            c_c += 1
        elif n_c[i] < con[i]:
            ck_nc = ck_nc + 1

    if ck_nc > c_c:
        return 0
    elif ck_nc < c_c:
        return 1
    else:
        return None





if __name__ == '__main__':
    choices = ['not confess', 'confess']
    s = {'Lobha': [[3, 10], [1, 5]], 'Raga': [[3, 10], [1, 5]]}
    p = 'Lobha'
    r = rational_decision(s, p)
    print(p, ':', choices[r])