//---------------------------------------------------------------------------------------
//-------------------Author : itsjaysuthar ----------------------------------------------
//---------------------------------------------------------------------------------------

#include<bits/stdc++.h>
using namespace std;

#define ll double

int main(){
    ll d,c=0;
    cin>>d;
    while(d--){
        ll r,h;
        cin>>r>>h;
        ll run=100*h;
        ll pari = 2 * 22/7.0 * r;
        if(run >= pari){
            c++;
        }
    }
    cout<<c<<endl;
return 0;
}
