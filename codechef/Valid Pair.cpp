//---------------------------------------------------------------------------------------
//-------------------Author : itsjaysuthar ----------------------------------------------
//---------------------------------------------------------------------------------------

#include<bits/stdc++.h>
using namespace std;

#define ll long long


int main()
{
    ll a,b,c;
    cin>>a>>b>>c;
    if((a>=1 && a<=10)&&(b>=1 && b<=10)&&(c>=1 && c<=10))
    {
        if(a==b || b==c || a==c)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
 	return 0;
}
