
#include "Arduino.h"

const int pinTrigger = 2;
const int pinEcho = 4;
const int pinled = 13;

void switchOnLed()
{
    digitalWrite(pinled, HIGH);
}

void switchOffLed()
{
    digitalWrite(pinled, LOW);
}

int getDistance()
{
    long distance = 0;
    long duration = 0;

    // send a 10us+ pulse
    digitalWrite(pinTrigger, LOW);
    delayMicroseconds(20);
    digitalWrite(pinTrigger, HIGH);
    delayMicroseconds(10);
    digitalWrite(pinTrigger, LOW);
    delayMicroseconds(20);

    //  read duration of echo
    duration = pulseIn(pinEcho, HIGH);
    distance = duration / 29.1;

    return(distance);
}

void setup()
{
  // initialize serial comms
  Serial.begin(9600);

  // set pins
  pinMode(pinTrigger, OUTPUT);
  pinMode(pinEcho, INPUT);
  pinMode(pinled, OUTPUT);
}

void loop()
{
    int distance=getDistance();

    Serial.write("distance: ");
    Serial.print(distance);
    Serial.write(" cm\n");

    if (distance < 10) {
        switchOnLed();
    }
    else {
        switchOffLed();
    }

    // wait
    delay(70);
}
