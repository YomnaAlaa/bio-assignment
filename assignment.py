# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "YOMNA"
__date__ = "$Mar 13, 2017 5:10:31 PM$"

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
    "GAC":"D",
    "GAG":"E",
    "GAU":"D",
    "GCA":"A",
    "GCC":"A",
    "GCG":"A",
    "GCU":"A",
    "GGA":"G",
    "GGC":"G",
    "GGG":"G",
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

    RNA = input("Enter the RNA sequence: ")
    length = len(RNA)
    amino = []
    K = 0
    j=3
    print(length)
    for i in range (0,length,3):
        TMP = RNA[i:j]

        if TMP not in RNADic:
            print("this is not in dictionary")
            break

        if TMP=="UAG" or TMP=="UGA" or TMP=="UAA":
            amino.append(" ")
        else:
            amino.append(RNADic[TMP])
            j = j + 3

    aminostring = ''.join(amino)
    print(amino)
    print(aminostring)
