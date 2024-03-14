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
    d = {}
    with open(fname, 'r') as f:
        for line in f:
            k, v = line.split('=')
            if v[-1] == '\n':
                v = v[:-1]
            d[k] = v

    return d

def codon(codon_table, gene):
    cod_tab = read_codons(codon_table)

    # Read DNA sequence first
    dna = ""

    # print(dna) # to check whether the reading is fine.

    # Translate each 3-letter set in DNA sequence to an amino acid
    polypep = []

    return polypep

if __name__ == '__main__':
    res = codon('codons.txt', 'homo_sapiens_mitochondrion.txt')
    print(res)

    # Try this too. Note.
    # This is a long sequence with MULTIPLE LINES.
    # res = codon('codons.txt', 'homo_sapiens_insulin.txt')
    # print(res)

