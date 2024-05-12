#include "ObserverUebung.h"
#include "dashboard.h"

TemperaturSensor::TemperaturSensor()
{
    
    //Datenarray mit Zufallswerten füllen
    srand(time(NULL));
    for(int i = 0 ; i < 5; i++)
    {
        data[i] = (double) (rand() % 501)/10.0;
    }
}

TemperaturSensor::~TemperaturSensor()
{
    cout << "Objekt gekillt" << endl;
}

string TemperaturSensor::getSensorType()
{
    return "Temperatur";
}

void TemperaturSensor::fetchData(double a[])
{
    //ToDo
    for(int i = 0 ; i < 10; i++)
    {
        a[i] = data[i];
    }
}

int TemperaturSensor::dataSize()
{
    return 5;
}


void TemperaturSensor::attach(Dashboard* d)
{
    //Mit Schleife ersten freien Platz in Observer-Array suchen
    int i = 0;
    do
    {
        if(observer[i] == NULL)
        {
            observer[i] = d;
            cout << "i: " << i << " : " << d << endl;
            break;
        }
        else
            i++;
    }while(i < 10);
}

void TemperaturSensor::detach(Dashboard* d)
{
    //Finde Index der Position von d
    int startIndex = -1;
    int endIndex = 9;

    for(int i = 0 ; i<10; i++)
        if(observer[i] == d)
            startIndex = i;
        else if(observer[i] == NULL)
        {
            endIndex = i;
            break;
        }
    // Nur falls das Element gefunden wurde
    if(startIndex >= 0)
    {
        cout << "startIndex: "<<startIndex<<" endIndex: "<<endIndex<< endl;
        // Lösche Element durch Überschreiben
        for(int i = startIndex; i < endIndex  ; i++)
        {
            cout << "i: " << i << " alt: " << observer[i] << " neu: " << observer[i+1] << endl;
            observer[i] = observer[i+1];
        }
        observer[endIndex] = NULL;
    }
}

void TemperaturSensor::notify()
{
    for (int i=0; i<10; i++)
    {
        if (observer[i]!= NULL)
        observer[i]->update();
    }

}
int TemperaturSensor::getState()
{
    //ToDo
    return 999;
}