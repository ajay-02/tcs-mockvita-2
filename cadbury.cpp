#include<iostream>
using namespace std;
int no_child(int r,int c){
  int count=0;
  int total=r*c;
  while(r && c){
    count++;
    if(r>c)
      r=r-c;
    else
      c=c-r;
  }
  return count;
}
int main(){
  int s=0;
  int minl,laxl,minw,maxw;
  cin>>minl>>maxl>>minw>>maxw;
  if(0<minl<1501 && 0<maxl<1501 && 0<minw<1501 && 0<maxw<1501){
    for(int i=minl;i<=maxl;i++){
      for(int j=minw;j<=maxw;j++){
        s=s+no_child(i,j);
      }
    }
  }
  cout<<s;
  return 0;
}