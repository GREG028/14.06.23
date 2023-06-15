#include <iostream>
using namespace std;

int main(){
    unsigned x;
    cout<<"KONFIGURACJA"<<endl<<"Podaj ilosc serdnii, ktore ma obliczac program"<<endl;
    cin>>x;
    unsigned l[x],p=0;
    cout<<"Wpisz dlugosc serdnii (podawaj malejaco, bez powtorek)..."<<endl;
    do{
        cout<<"nr "<<p+1<<": ";
        cin>>l[p];
    }while(++p<x);
    p=0;
    double m[l[0]],s[x];
    s[x-1]=0;
    cout<<"Witaj w programie obliczajacym duzo serdnii !!! (najpierw musisz wpisac "<<l[0]<<" wartosci !!!)"<<endl;
    p=l[0];
    do{
        cin>>m[--p];
    }while(p);
    unsigned i=x;
    cout<<"p - "<<p<<endl;
    while(--i){
        do{
            s[i]+=m[p++];
        }while(p<l[i]);
        s[i-1]=s[i];
    }
    do{
        s[0]+=m[p++];
    }while(p<l[0]);
    i=x;
    do{
        cout<<"Serdnia z "<<l[--i]<<" to "<<s[i]/l[i]<<" !!!"<<endl;
    }while(i);
    cout<<"Swietnie !!! Teraz mozemy liczyc nowa serdnie po kazdej wpisanej wartosci !!!"<<endl<<"Dawaj NAN"<<endl;
    do{
        p=(p+l[0]-1)%l[0];
        s[0]-=m[p];
        cin>>m[p];
        i=x;
        while(--i){
            s[i]+=m[p]-m[(p+l[i])%l[0]];
            cout<<"Serdnia z "<<l[i]<<" to "<<s[i]/l[i]<<" !!!"<<endl;
        }
        s[0]+=m[p];
        cout<<"Serdnia z "<<l[0]<<" to "<<s[0]/l[0]<<" !!!"<<endl;
    }while(true);
}