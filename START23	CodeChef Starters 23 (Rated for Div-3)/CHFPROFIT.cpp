#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,x,y,z;
	cin>>t;
	while(t--)
	{
	    int priceBefore,priceAfter,res=0;
	    cin>>x>>y>>z;
	    priceBefore=x*y;
	    priceAfter=x*z;
	    res=priceAfter-priceBefore;
	    cout<<res<<endl;
	}
	
	return 0;
}
