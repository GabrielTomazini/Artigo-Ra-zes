import matplotlib.pyplot as plt
def calculaRaizRecorrencia(n, ini):
    seq = []
    x = []
    for i in range(30):
        x.append(i)
    for i in range(30):
        ini = (1/2)*(ini + (n/ini))
        seq.append(ini)
    plt.plot(x,seq)
    plt.xlabel('Numero iterações')
    plt.ylabel('Valores Raiz')
    plt.show()
    print("raiz de ",n,"é: ",seq[-1])
    print("seq:",seq)

calculaRaizRecorrencia(5, 1)