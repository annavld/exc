#include <stdio.h>

int main()
{
    int g[100];
    int nStelle, iStelle,aTeiler;
    
    //for (int iStelle = 0; iStelle<100;iStelle++) //Alle Türen werden geöffnet
    //{
    //    g[iStelle]=0;
    //}
    
    for (int aTeiler = 1; aTeiler < 10; aTeiler++)
    {
        for (int nStelle = 0; nStelle<10;nStelle++)
        {
            if ((nStelle+1)%aTeiler==0) //die nTe Tür soll...
            {
               g[nStelle-1]=1; //...geschlossen werden
               printf("%d Türen \n",g[nStelle]);
            }
            
        }    
    }  
    
    printf("%d Tür",g[nStelle]);
    return 0;
}