#include <hcsr04.h>



HCSR04 hc(9,8);//initialisation class HCSR04 (trig pin , echo pin)

void setup()
{ Serial.begin(9600); }

void loop() 
{ 
  Serial.println( hc.dist() ); //return current distance (cm) in serial
  delay(100); 
} 
