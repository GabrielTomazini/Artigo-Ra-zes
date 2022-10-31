import matplotlib.pyplot as plt
def calculaRaizBabilonica(n, err, apr):
    i = 0
    a = 0
    b = n/apr
    values = []
    it = []
  # while( err < abs((m.pow(b,2) - n))):
    for x in range(0,30):
        ak = (a + b)/2
        b = n/ak
        a = ak
        i = i + 1
        it.append(i)
        values.append(b)
    plt.plot(it,values)
    plt.ylabel('Aproximações para a raiz')
    plt.xlabel('Iterações')
    plt.show()
    print("Iteracoes:", i)
    print("Vetor iteracoes:",it)
    print("Vetor numeros",values)
    print(" Aproximação para a raiz é: ")
    print('%.60f' % b)
    
n = 2
err = 10**-4
apr = 1
calculaRaizBabilonica(n,err,apr)
