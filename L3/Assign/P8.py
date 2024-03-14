"""
Write a function named codon.
The function takes 2 arguments:
a file name of a codon table (as string)
and a file name of a DNA sequence, reads the two files,
uses a codon table to decipher the DNA sequence to a protein,
and returns a list of the deciphered sequence of amino acids.
The codon table file is a simple text file,
written in a simple format:
each line contains one codon and its corresponding amino acid
with a "=" in between.
(Note: fun gene data can be downloaded from
NCBI GenBank, looking for download "FASTA")
"""

def read_codons(fname):
    a = {}
    with open(fname, 'r') as f:
        for line in f:
            j, v = line.split('=')
            if v[-1] == '\n':
                v = v[:-1]
            a[j] = v

    return a

def codon(codon_table, gene):
    cod_tab = read_codons(codon_table)

    # Read DNA sequence first
    dna = ""
    list = []
    polypep = []
    check = []
    with open(gene, "r")as f:
        for line in f:
            line = line.replace("\n", "")
            list.append(line)
        list.pop(0)
        dna = "".join(list)
        for i in dna:
            check.append(i)
            if len(check) == 3:
                same = "".join(check)
                if same in cod_tab:
                    polypep.append(cod_tab[same])
                    for j in range(3):
                        check.pop(0)



    # print(dna) # to check whether the reading is fine.

    # Translate each 3-letter set in DNA sequence to an amino acid

    return polypep

if __name__ == '__main__':
    res = codon('codons.txt', 'homo_sapiens_mitochondrion.txt')
    print(res)
    print(len(res))

    # Try this too. Note.
    # This is a long sequence with MULTIPLE LINES.
    # res = codon('codons.txt', 'homo_sapiens_insulin.txt')
    # print(res)

