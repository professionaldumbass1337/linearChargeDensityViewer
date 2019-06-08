import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def delSpace(string):
    n = len(string)
    newStr = ""
    aa = ['D','T','S','E','P','G','A','C','V','M','I','L','Y','F','H','K','R','W','Q','N']
    for i in range(n):
        if string[i] in aa:
            newStr += string[i]
    return newStr


def main():
    string = """
    MLPGVGLTPSAAQTARQHPKMHLAHSTLKPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVY
    SQVVFSGKAYSPKATSSPLYLAHEVQLFSSQYPFHVPLLSSQKMVYPGLQEPWLHSMYHGAAFQLTQGDQLSTHTDG
    IPHLVLSPSTVFFGAFAL      
    """
    string = delSpace(string)
    w = 20
    
    f = {'D':-1,'T':0,'S':0,'E':-1,'P':0,'G':0,'A':0,'C':-0.1,'V':0,'M':0,'I':0,'L':0,'Y':0,'F':0,'H':0.1,'K':1,'R':1,'W':0,'Q':0,'N':0}
    indivisualCharge = []
    label = []
        
    for i in range(len(string)-(w-1)):
        sum = 0
        for j in range(i,i+w):
            sum += f[string[j]]   
        indivisualCharge.append(sum)
        label.append(str(i+1) + "~" + str(i+w))
        

    fig, ax = plt.subplots()
    ax.plot(label, indivisualCharge)

    ax.set(xlabel='Window Index', ylabel='Charge',
        title='Charge Density')

    ax.set_xticklabels(label, rotation=45 )

    plt.show()


if __name__ == "__main__":
    main()
