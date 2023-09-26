#include <iostream>
using namespace std;

int p1();
int p2();
char v0='0',v1='1',v2='2',v3='3',v4='4',v5='5',v6='6',v7='7',v8='8';
string per1,per2;
char t1,t2,n,m;
int a=0,b=0;

int main()
{
    cout<<"The tic tac toe game \n";
    cout<<"enter the first person name\n";
    cin>>per1;
    cout<<"enter the second person name \n";
    cin>>per2;
    cout<<"first person enter your tool    ( X or O )";
    cin>>t1;
    if (t1=='X')
        t2='O';
    else
        t2='X';
        
    cout<<v0<<" | "<<v1<<" | "<<v2<<"\n----------\n"<<v3<<" | "<< v4<<" | "<< v5<<"\n----------\n"<<v6<<" | "<<v7<<" | "<< v8<<"\n";
    
    int i=0;
    while(a!=2 && b!=2 )
    {
    cout<<per1<<" it's your turn";
    cin>>n;
    if(n=='0')
        v0=t1;
    else if(n=='1')
         v1=t1;
    else if(n=='2')
        v2=t1;
    else if(n=='3')
        v3=t1;
    else if(n=='4')
        v4=t1;
    else if(n=='5')
        v5=t1;
    else if(n=='6')
        v6=t1;
    else if(n=='7')
        v7=t1;
    else 
        v8=t1;
    a=p1();
     
    cout<<v0<<" | "<<v1<<" | "<<v2<<"\n----------\n"<<v3<<" | "<< v4<<" | "<< v5<<"\n----------\n"<<v6<<" | "<<v7<<" | "<< v8<<"\n";
    if(a==2){
        break;
    }

    cout<<per2<<" it's your turn";
    cin>>m;
    if(m=='0')
        v0=t2;
    else if(m=='1')
        v1=t2;
    else if(m=='2')
        v2=t2;
    else if(m=='3')
        v3=t2;
    else if(m=='4')
        v4=t2;
    else if(m=='5')
        v5=t2;
    else if(m=='6')
        v6=t2;
    else if(m=='7')
        v7=t2;
    else 
        v8=t2;
    
    b=p2();
    
    cout<<v0<<" | "<<v1<<" | "<<v2<<"\n----------\n"<<v3<<" | "<< v4<<" | "<< v5<<"\n----------\n"<<v6<<" | "<<v7<<" | "<< v8<<"\n";
    i++;
    }
}

int p1()
    {
    if((v0==v1 && v1==v2) || (v0==v3 && v3==v6) || (v0==v4 && v4==v8) || (v6==v7 && v7==v8) || (v6==v4 && v4==v2) || (v8==v5 && v5==v2) || (v3==v4 && v4==v5))
        {
        cout<<"\n"<<per1<<" you won\n";
        return 2;
        }
    }

int p2(){
    if((v0==v1 && v1==v2) || (v0==v3 && v3==v6) || (v0==v4 && v4==v8) || (v6==v7 && v7==v8) || (v6==v4 && v4==v2) || (v8==v5 && v5==v2) || (v3==v4 && v4==v5))
        {
        cout<<"\n"<<per2<<" you won\n";
        return 2;
        }
    }