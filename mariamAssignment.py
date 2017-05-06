if __name__ == "__main__":
    RNADic = {"AAA": "K",
    "AAC": "N",
    "AAG": "K",
    "AAU":"N",
    "ACA":"T",
    "ACC":"T",
    "ACG":"T",
    "ACU":"T",
    "AGA":"R",
    "AGC":"S",
    "AGG":"R",
    "AGU":"S",
    "AUA":"I",
    "AUC":"I",
    "AUG":"M",
    "AUU":"I",
    "CAA":"Q",
    "CAC":"H",
    "CAG":"Q",
    "CAU":"H",
    "CCA":"P",
    "CCC":"P",
    "CCG":"P",
    "CCU":"P",
    "CGA":"R",
    "CGC":"R",
    "CGG":"R",
    "CGU":"R",
    "CUA":"L",
    "CUC":"L",
    "CUG":"L",
    "CUU":"L",
    "GAA":"E",
    "GAU":"D",
    "GCA":"A",
    "GCC":"A",
    "GCG":"A",
    "GCU":"A",
    "GGA":"G",
    "GGC":"G",
    "GGG":"G",
    "GAC":"D",
    "GAG":"E",
    "GGU":"G",
    "GUA":"V",
    "GUC":"V",
    "GUG":"V",
    "GUU":"V",
    "UAA":"stop",
    "UAC":"Y",
    "UAG":"stop",
    "UAU":"Y",
    "UCA":"S",
    "UCC":"S",
    "UCG":"S",
    "UCU":"S",
    "UGA":"stop",
    "UGC":"C",
    "UGG":"W",
    "UGU":"C",
    "UUA":"L",
    "UUC":"F",
    "UUG":"L",
    "UUU":"F"}

rna = input ("enter the rna seq")
len = len(rna)
amino = []
j = 3

for i in range(0, len, 3):
    if rna[i:j] not in RNADic:
        print("not in dictionary")
        break
    if rna[i:j] == "UAG" or rna[i:j] == "UGA" or rna[i:j] == "UAA":
        break
    else:
        amino.append(RNADic[rna[i:j]])
        j = j + 3
print(amino)

