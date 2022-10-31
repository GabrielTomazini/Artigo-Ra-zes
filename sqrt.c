#include <iostream>
#include <cmath>
#include <locale.h>
#include <iomanip>
using namespace std;

void calculaRaizBabilonico(long double num, long double err, long double apr){

    long double a = 0, b = num/apr,ak;
    while( err < abs((pow(b,2) - num))){
        ak = (a + b)/2;
        b = num/ak;
        a = ak;
    }
    cout << " Aproxima��o para a raiz �: " << fixed << setprecision(20) << b << endl;
}
int main()
{
    setlocale(LC_ALL, "Portuguese");
    double num,err,apr;
    err = pow(10,-4);
    cout << "Digite um n�mero para c�lculo aproximado da raiz: ";
    cin >> num;
    cout << "Digite uma aproxima��o inicial: ";
    cin >> apr;
    cout<< err;
    calculaRaizBabilonico(num,err,apr);
    return 0;
}
