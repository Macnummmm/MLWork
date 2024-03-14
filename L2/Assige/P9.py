
def count_kmer ( kmr,tx ):
    ct = 0
    st = 0  
    while st < len ( tx ) :
        r = tx.find ( kmr,st )
        if r != -1:
            st = r +1
            ct += 1
        else:
            break      
    return ct

if __name__ == "__main__":
    r = count_kmer('ACTAT', 'ACAACTATGCATACTATCGGGAACTATC')
    print(r)
    r = count_kmer('AC', 'ACAACTATGCATACTATCGGGAACTATC')
    print(r)
    r = count_kmer('ATA', 'CGATATATCCATAG')
    print(r)