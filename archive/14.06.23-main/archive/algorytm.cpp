#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main(){

    fstream fin;
  
    // Open an existing file
    fin.open("AAPL.csv", ios::in);

    
    unsigned p=0,l;
    float dane[5] = {122.720001, 123.080002, 122.940002, 122.25, 123.75};
    cout<<"Aby rozpoczac, wpisz dlugosc serdnii, ktora ma obliczac program"<<endl;
    cin>>l;
    double m[l],s=0;
    //cout<<"Witaj w programie obliczajacym serdnie z "<<l<<" !!!"<<endl<<"Dawaj "<<l<<endl;
    do{
        s+=dane[p];
    }while(++p<l);
    cout<<"Swietnie !!! Teraz mozemy liczyc nowa serdnie po kazdej wpisanej wartosci !!!"<<endl<<"Dawaj NAN"<<endl;
    do{
        cout<<"Twoja serdnia to "<<s/l<<" !!!"<<endl;
        p=(p+1)%l;
        s-=dane[p];
        cin>>dane[p];
        s+=dane[p];
    }while(true);
}
