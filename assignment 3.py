Antibiotics = {
    'G':57,
    'A':71,
    'S':87,
    'P':97,
    'V':99,
    'T':101,
    'C':103,
    'I':113,
    'L':113,
    'N':114,
    'D':115,
    'K':128,
    'Q':128,
    'E':129,
    'M':131,
    'H':137,
    'F':147,
    'R':156,
    'Y':163,
    'W':186
}

def MassSpectrum (peptide):
    length = len(peptide)
    summ = 0
    J = 1
    for i in range (0, length, 1):
        summ = summ + Antibiotics[peptide[i:J]]
        J = J+1
    return summ

def Subpeptides (pep):
    length = len(pep)
    sub = []
    j=0
    sub.append("")
    for i in range(0,length-1,1):
        j = j+1
        f = j
        for k in range (0, length, 1):
            if (k>f):
                temp1 = pep[k:length]
                temp2 = pep[0:f]
                temp3=[]
                temp3.append(temp1)
                temp3.append(temp2)
                temp4 = ''.join(temp3)
                sub.append(temp4)
            else:
                sub.append(pep[k:f])
            f = (f + 1) % length
    sub.append(pep)
    return sub

if __name__ == "__main__":
    QE = input("Enter The Antibiotic: ")
    q = Subpeptides(QE)
    length = len(q)
    result = []
    for i in range (0,length,1):
        summation = MassSpectrum(q[i])
        result.append(summation)
    result.sort()
    print(result)

