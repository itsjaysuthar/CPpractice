//---------------------------------------------------------------------------------------
//-------------------Author : itsjaysuthar ----------------------------------------------
//---------------------------------------------------------------------------------------

#include<bits/stdc++.h>
using namespace std;

#define ll long long

int main()
{
    ll t;
    cin>>t;
    if(t>=1 && t<=1000)
    {
        while(t--)
        {
            ll a,b,ans=0,d;
            cin>>a>>b;
            if((a>=1 && a<=1000000)&&(b>=1 && b<=1000000))
            {
                d=__gcd(a,b);
                ans=a*b/d;
                cout<<d<<" "<<ans<<endl;
            }

        }
    }

 	return 0;
}