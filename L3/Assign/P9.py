def sweet(fsweet, fdrink):

    # Retrieve sweetness dict
    sweetness = {}
    sweetness_d = {}
    
    # Write your code!

    with open(fsweet, "r") as d:
        one = True
        for i in d:
            if one :
                one = False
            else:
                sub, swtness, cal = i.split()
                sweetness[sub] = float(swtness)

    with open(fdrink, 'r+') as fs:
        for line in fs:
            sub_d, swtness_d = line.split()
            sweetness_d[sub_d] = float(swtness_d)
    # Print to check if we retrieve it ok.
    # hint: having a number as float is more convenient later
    

    # Calculate the estimated sweetness
    sweet_sum = 0
    for i in sweetness_d:
        if i in sweetness:
            sweet_sum += sweetness[i] * sweetness_d[i]
            
    # write/append message to the end of file
    msg = "\nSweet as {:.1f}% sucrose solution".format(sweet_sum)

    with open (fdrink, "a+") as coca:
        coca.write(msg)

if __name__ == '__main__':
    sweet('sweetness1.txt', 'CocaPanda.txt')