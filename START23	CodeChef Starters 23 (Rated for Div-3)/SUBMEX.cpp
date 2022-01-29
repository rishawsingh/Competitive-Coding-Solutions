#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,x,n,k;
	cin>>t;
	while(t--)
	{
	    int res=0;
	    cin>>n>>k>>x;
	    if(x>k)
	    {
	        cout<<"-1\n"<<endl;
	    }
	    else
	    {
	        int count=0;
	        for(int i=0;i<n;i++)
	        {
	            if(count==x)
	            count=0;
	            cout<<count<<" ";
	            count++;
	        }
	        cout<<endl;
	    }

	}
	
	return 0;
}
