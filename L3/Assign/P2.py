def cam_expos(a, b):
    f = ['f/1.4', 'f/2', 'f/2.8', 'f/4', 'f/5.6', 'f/8', 'f/11', 'f/16', 'f/22']
    st = ['1/4', '1/8', '1/15', '1/30', '1/60', '1/125', '1/250', '1/500', '1/1000', '1/2000', '1/4000']
    iso = ['100', '200', '400', '800', '1600', '3200']

    sf = f.index(a[0]) - f.index(b[0])
    ss = st.index(a[1]) - st.index(b[1])
    si = iso.index(b[2]) - iso.index(a[2])
    total = sf + ss + si

    return sf, ss, si, total

if __name__ == '__main__':
    res = cam_expos(['f/2.8', '1/500', '400'], ['f/5.6', '1/125', '200'])
    print(res)