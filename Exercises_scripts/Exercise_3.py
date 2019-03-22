#!/home/user/miniconda3/bin/python

## Finding the square of prime numbers between 1&100

Prime_numbers=range(1,100)
[i**2 for i in range(1,100) if i%3==0]

## Finding the reverse complement of "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"

template = "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
print(template)

rev_template=list(template)
rev_template.reverse()
rev_template

d={"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
Reverse_complement=[d[i] for i in template]
print(Reverse_complement)

#"".join(Reverse) #This is an undefined variable, should have been: -1

print("".join(Reverse_complement)) 

#CK: You also needed to print the reverse complement -1
