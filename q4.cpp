#include<iostream>
using namespace std;

int main(){

    int w[5][3] = {3,4,6,
                   4,5,7,
                   3,4,6,
                   7,10,15,
                   5,7,10};
    int z[5],f[14],x[5];
    float ufp,caf,fp;
    
    cout<<"Enter User Inputs & its complexity factor (0 for low, 1 for avg, 2 for high) : "; cin>>z[0]>>x[0];
    cout<<"Enter User Output & its complexity factor (0 for low, 1 for avg, 2 for high) : "; cin>>z[1]>>x[1];
    cout<<"Enter User Inquires & its complexity factor (0 for low, 1 for avg, 2 for high) : "; cin>>z[2]>>x[2];
    cout<<"Enter Logical Files & its complexity factor (0 for low, 1 for avg, 2 for high) : "; cin>>z[3]>>x[3];
    cout<<"Enter Interface files & its complexity factor (0 for low, 1 for avg, 2 for high) : "; cin>>z[4]>>x[4];
    
    cout<<"\n Enter 14 factors in order :: \n";
    for(int i=0;i<14;i++) cin>>f[i];
    int tmp=0;
    for(int i=0;i<14;i++) tmp+=f[i];
    caf = 0.65 + 0.01*tmp;
    
    ufp=0;
    for(int i=0;i<5;i++) ufp+=w[i][x[i]]*z[i];
    
    cout<<"\n ---  values ---  \n caf & ufp :: "<<caf<<' '<<ufp<<'\n';
    
    fp = caf * ufp;
    
    cout<<"\nFunction point value = "<<fp<<"\n";
    return 0;
}
