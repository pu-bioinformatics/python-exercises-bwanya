#!/home/user/miniconda3/bin/python

## Calculating the % GC content in 'AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA' using functions.

seq="AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA"
def percentGC(seq):
    seq_length=len(seq)
    G = seq.count('G')
    C = seq.count('C')
    percent_GC = ((G+C)/seq_length)*100 # do not use the same variable name as your function -1
    return(percent_GC)

#CK: You need to call the function -1

print(percentGc(seq))

## CK: You also need a function that tests if the sequence is valid -1