# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "YOMNA"
__date__ = "$Mar 13, 2017 5:10:31 PM$"

if __name__ == "__main__":
    RNADic = {"AAA": "K",
              "AAC": "N",
              "AAG": "K",
              "AAU": "N",
              "ACA": "T",
              "ACC": "T",
              "ACG": "T",
              "ACU": "T",
              "AGA": "R",
              "AGC": "S",
              "AGG": "R",
              "AGU": "S",
              "AUA": "I",
              "AUC": "I",
              "AUG": "M",
              "AUU": "I",
              "CAA": "Q",
              "CAC": "H",
              "CAG": "Q",
              "CAU": "H",
              "CCA": "P",
              "CCC": "P",
              "CCG": "P",
              "CCU": "P",
              "CGA": "R",
              "CGC": "R",
              "CGG": "R",
              "CGU": "R",
              "CUA": "L",
              "CUC": "L",
              "CUG": "L",
              "CUU": "L",
              "GAA": "E",
              "GAC": "D",
              "GAG": "E",
              "GAU": "D",
              "GCA": "A",
              "GCC": "A",
              "GCG": "A",
              "GCU": "A",
              "GGA": "G",
              "GGC": "G",
              "GGG": "G",
              "GGU": "G",
              "GUA": "V",
              "GUC": "V",
              "GUG": "V",
              "GUU": "V",
              "UAA": "stop",
              "UAC": "Y",
              "UAG": "stop",
              "UAU": "Y",
              "UCA": "S",
              "UCC": "S",
              "UCG": "S",
              "UCU": "S",
              "UGA": "stop",
              "UGC": "C",
              "UGG": "W",
              "UGU": "C",
              "UUA": "L",
              "UUC": "F",
              "UUG": "L",
              "UUU": "F"}

    # -------------------------------------TILL HERE IS THE CONVERTION BETWEEN DNA TO RNA--------------------------------------------------
    RCDNA = input("Enter the DNA sequence: ")
    length = 0
    pro = input("Enter the protein: ")
    amino = []
    RNA = []
    RESULT = []
    K = 0
    j=1
    summ=0
    W=0
    DNA = ""
    for V in range (0,3,1):
        K = 0
        j = 1
        summ = 0
        RNA[:] = []
        amino[:] = []
        if V==0:
            summ=0
            DNA = RCDNA
        elif V==1:
            summ=1
            DNA = RCDNA[1:]
        elif V==2:
            summ=2
            DNA = RCDNA[2:]
        print ("DNA IS:",DNA)
        length = len(DNA)

        for i in range(0, length, 1):
            TMP = DNA[i:j]
            if TMP == "T":
                RNA.append("U")
            else:
                RNA.append(TMP)
            j = j + 1


        RNASTR = ''.join(RNA)
        print("RNA IS:",RNASTR)
# --------------------------------------------converting the original RNA-----------------------------------------------------------
        H = 3
        for i in range (0,length,3):
            TMP = RNASTR[i:H]
            if TMP not in RNADic:
                print("this is not in dictionary")
                break

            if TMP=="UAG" or TMP=="UGA" or TMP=="UAA":
                amino.append(" ")
                H = H +3
            else:
                amino.append(RNADic[TMP])
                H = H + 3

        aminostring = ''.join(amino)
        print("PROTEIN IS:",aminostring)
# --------------------------------------------FINDING THE PROTEIN IN DNA-----------------------------------------------------------
        import re

        for m in re.finditer(pro, aminostring):
            STRAT = m.start()*3+summ
            END = m.end()*3+summ
            print("this protein is found at index:",STRAT," -> ",DNA[STRAT:END])
            GHY = []
            GHY.append(str(STRAT))
            GHY.append(" ")
            GHY.append(RCDNA[STRAT:END])
            HGG = ''.join(GHY)
            RESULT.append(HGG)
        print()

        del RNASTR
        del aminostring
# --------------------------------------------getting second DNA-----------------------------------------------------------

    RCDNA2 = RCDNA
    lenn  = len(RCDNA2)
    RCDNA2 = RCDNA2[::-1]
    print(RCDNA2)
    RRDNA1 = []

    P=0
    O = 1
    for h in range(0,lenn,1):
        TMP2 = RCDNA2[P:O]
        if TMP2=="A":
            RRDNA1.append("T")
        elif TMP2=="T":
            RRDNA1.append("A")
        elif TMP2=="G":
            RRDNA1.append("C")
        elif TMP2=="C":
            RRDNA1.append("G")
        P = P+1
        O = O+1

    print("rrr=",RRDNA1)
    RRDNA2= ''.join(RRDNA1)
    print("reversed RNA is:",RRDNA2)

#-----------------------------------------GETTING ALL COMBINATIONS OF SECOND RNA------------------------------------------------------
    for V in range(0, 3, 1):
        K = 0
        j = 1
        summ = 0
        RNA[:] = []
        amino[:] = []
        if V == 0:
            summ = 0
            DNA = RRDNA2
        elif V == 1:
            summ = 1
            DNA = RRDNA2[1:]
        elif V == 2:
            summ = 2
            DNA = RRDNA2[2:]
        print("DNA IS:", DNA)
        length = len(DNA)

        for i in range(0, length, 1):
            TMP = DNA[i:j]
            if TMP == "T":
                RNA.append("U")
            else:
                RNA.append(TMP)
            j = j + 1

        RNASTR = ''.join(RNA)
        print("RNA IS:", RNASTR)
#--------------------------------------------CONVERTING TO PROTEIN-----------------------------------------------
        H = 3
        for i in range(0, length, 3):
            TMP = RNASTR[i:H]
            if TMP not in RNADic:
                print("this is not in dictionary")
                break

            if TMP == "UAG" or TMP == "UGA" or TMP == "UAA":
                amino.append(" ")
                H = H + 3
            else:
                amino.append(RNADic[TMP])
                H = H + 3

        aminostring = ''.join(amino)
        print("PROTEIN IS:", aminostring)
        print(RCDNA)

#-------------------------------------------SEARCHING IN THE SECOND RNA-------------------------------------------------------
        import re
        for m in re.finditer(pro, aminostring):
            STRAT = length - m.start() * 3 + summ-V
            END = length - m.end() * 3 + summ-V
            print("this protein is found at index:", END, " ->", RCDNA[END:STRAT])
            GHY = []
            GHY.append(str(END))
            GHY.append(" ")
            GHY.append(RCDNA[END:STRAT])
            HGG = ''.join(GHY)
            RESULT.append(HGG)
        print()
        del RNASTR
        del aminostring
        len1 = len(RESULT)

#----------------------------------SORTING THE ARRAY OF RESULTS AND PRINTING IT-----------------------------------------------------
    uu = []
    res = []
    for x in range(0, len1, 1):
        uu =[]
        gg = RESULT[x]
        for char in gg:
            if not(char.isalpha()) and not(char == " "):
                uu.append((char))
            elif char.isalpha():
                break
        print(uu)
        hj = ''.join(uu)
        res.append(int(hj))

    res.sort()
    final = []
    for y in range(0, len1, 1):
        gg1 = str(res[y])
        for y1 in range(0, len1, 1):
            if RESULT[y1].__contains__(gg1):
                final.append(RESULT[y1])
                break
    print(final)
    lp=0
    for oop in range (0,len1,1):
        charTemp = ((final[oop]))
        for char in charTemp:
            if not(char.isalpha()):
                lp=lp+1
            elif char.isalpha():
                break
        print(final[oop][lp:])
        lp=0