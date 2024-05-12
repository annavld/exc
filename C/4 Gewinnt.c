#include <stdio.h>
 
int main()
{
  char feld [5][6];
  int z,s,n;
  char playerone = 'X';
  char playertwo = 'Y';
  char winningplayer;
  int changeplayer = 1;
  int platzabfrage = 0;
  int spieldauer = 0;
  int chosencolumn;
  int zeile = 0;
  
  while (spieldauer == 0) 
  {
      for (n=0; n<7;n++)
      {
          printf("%3i ",n);
      }
      
      for (z=0; z<6; z++)
      {
         printf("\n*---*---*---*---*---*---*---*\n|");
          
          for (s=0; s<7;s++)
          {
              if (feld [z][s]=='X') 
              {
                 printf("X  |");
              }
              else if (feld [z][s]=='Y')
              {
                 printf("Y  |");
              }
              else 
              {
                  printf("   |");
              }
          }
      }
      printf("\n*---*---*---*---*---*---*---*\n");
      
      if (changeplayer==1)
      {
          while (platzabfrage ==0) 
        { 
            printf("Spieler 1 (X), bitte Spaltennummer eingeben: \n");
            scanf("%d",&chosencolumn);
            
                for (zeile=5;zeile >=0;zeile--)
                {
                    if (feld[zeile][chosencolumn]!='X' && feld[zeile][chosencolumn]!='Y') 
                      {
                          feld [zeile][chosencolumn]='X';
                          platzabfrage = 1;
                          break;
                      }
                      else if (zeile==0)
                      {
                          printf("Bitte wählen Sie eine andere Spaltennummer.\n");
                      }
                }
                zeile=5;
        }
        platzabfrage = 0;
        changeplayer = 2;
        
      }
    else if (changeplayer==2)
    {
         while (platzabfrage ==0) 
        { 
            printf("Spieler 2(Y), bitte Spaltennummer eingeben: \n");
            scanf("%d",&chosencolumn);
            
                for (zeile=5;zeile>=0;zeile--)
                {
                    if (feld[zeile][chosencolumn]!='X' && feld[zeile][chosencolumn]!='Y') 
                      {
                          feld [zeile][chosencolumn]='Y';
                          platzabfrage = 1;
                          break;
                      }
                      else if (zeile==0)
                      {
                          printf("Bitte wählen Sie eine andere Spaltennummer.\n");
                      }
                }
                zeile=5;
        }
        platzabfrage = 0;
        changeplayer = 1;
    } 
    
    if (changeplayer==2)
    {
        winningplayer='X';
    }
    else if (changeplayer==1)
    {
        winningplayer='Y';
    }
    
    for (z=0; z<6; z++)
    {
        for (s=0; s<7;s++) //horizontale Gewinnabfrage
        {
            if(feld [s][z]==winningplayer 
            && feld[s+1][z]==winningplayer 
            && feld[s+2][z]==winningplayer
            && feld[s+3][z]==winningplayer)
            {
                printf("Sie haben gewonnen");
                spieldauer=1;
                break;
            }
            
        }
    }
    for (z=0; z<6; z++)
    {
        for (s=0; s<7;s++) //senkrechte Gewinnabfrage
        {
            if(feld [s][z]==winningplayer 
            && feld[s][z+1]==winningplayer 
            && feld[s][z+2]==winningplayer
            && feld[s][z+3]==winningplayer)
            {
                printf("Sie haben gewonnen");
                spieldauer=1;
                break;
            }
            
        }
    }
    for (z=0; z<6; z++)
    {
        for (s=0; s<7;s++) //diagonal nach links Gewinnabfrage
        {
            if(feld [s][z]==winningplayer 
            && feld[s-1][z-1]==winningplayer 
            && feld[s-2][z-2]==winningplayer
            && feld[s-3][z-3]==winningplayer)
            {
                printf("Sie haben gewonnen");
                spieldauer=1;
                break;
            }
            
        }
    }
    for (z=0; z<6; z++)
    {
        for (s=0; s<7;s++) //diagonal nach rechts Gewinnabfrage
        {
            if(feld [s][z]==winningplayer 
            && feld[s+1][z-1]==winningplayer 
            && feld[s+2][z-2]==winningplayer
            && feld[s+3][z-3]==winningplayer)
            {
                printf("Sie haben gewonnen");
                spieldauer=1;
                break;
            }
            
        }
    }
    system("clear"); 
    }
    return 0; 
}
