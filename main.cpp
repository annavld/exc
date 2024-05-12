#include <iostream>
#include "ObserverUebung.h"
#include "dashboard.h"

using namespace std;

int main()
{
    TemperaturSensor* t= new TemperaturSensor;

    Dashboard* d[10];
    //10 Observer
    for(int i=0; i<10;i++)
    {
        d[i] = new Dashboard_1;
        //Polymorphie: ich entscheide während der Laufzeit ob das Objekt real ist
        t->attach(d[i]);
    }
    
    cout << "----------------------\n";
    t->detach(d[0]);

    cout << "----------------------\n";
    t->detach(d[9]);

    cout << "----------------------\n";
    t->detach(d[8]);

    cout << "----------------------\n";
    t->detach(d[4]);
    
    cout << "----------------------\n";
    t->detach(d[4]);
    
    return 0;
 
}

