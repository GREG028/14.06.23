#include <iostream>
using namespace std;

int main(){
    unsigned x;
    cout<<"KONFIGURACJA"<<endl<<"Podaj ilosc serdnii, ktore ma obliczac program"<<endl;
    cin>>x;
    unsigned l[x],a[x],p=0;
    cout<<"Wpisz dlugosc oraz liczbe akcji przypisana do serdnii (podawaj malejaco, bez powtorek)..."<<endl;
    do{
        cout<<"nr "<<p+1<<": ";
        cin>>l[p]>>a[p];
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
    bool q[x];
    do{
        cout<<"Serdnia z "<<l[--i]<<" to "<<s[i]/l[i]<<" !!!"<<endl;
        q[i]=(s[i]<m[0]*l[i]);
    }while(i);
    cout<<"Swietnie !!! Teraz mozemy liczyc nowa serdnie po kazdej wpisanej wartosci !!!"<<endl<<"Dawaj NAN"<<endl;
    int z;
    do{
        p=(p+l[0]-1)%l[0];
        z=0;
        s[0]-=m[p];
        cin>>m[p];
        i=x;
        while(--i){
            s[i]+=m[p]-m[(p+l[i])%l[0]];
            cout<<"Serdnia z "<<l[i]<<" to "<<s[i]/l[i]<<" !!!"<<endl;
            if(q[i]){
                if(s[i]>m[p]*l[i]){
                    z-=a[i];
                    q[i]=0;
                }
            }
            else
                if(s[i]<m[p]*l[i]){
                    z+=a[i];
                    q[i]=1;
                }
        }
        s[0]+=m[p];
        if(q[0]){
            if(s[0]>m[p]*l[0]){
                z-=a[0];
                q[i]=0;
            }
        }
        else
            if(s[0]<m[p]*l[0]){
                z+=a[0];
                q[i]=1;
            }
        cout<<"Serdnia z "<<l[0]<<" to "<<s[0]/l[0]<<" !!!"<<endl;
        if(z){
            if(z<0)
                cout<<"SPRZEDAJ "<<-z<<" !!!";
            else
                cout<<"KUPUJ "<<z<<" !!!";
        }
    }while(true);
}