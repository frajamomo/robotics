// HC-SR04-test.ino
//
#include "Arduino.h"

int pinTrigger = 2;
int pinEcho = 4;
int led = 13;

void setup()
{
  // initialize serial comms
  Serial.begin(9600);

  // set pins
  pinMode(pinTrigger, OUTPUT);
  pinMode(pinEcho, INPUT);
  pinMode(led, OUTPUT);
}

void loop()
{
  // send a 10us+ pulse
  digitalWrite(pinTrigger, LOW);
  delayMicroseconds(20);
  digitalWrite(pinTrigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrigger, LOW);
  delayMicroseconds(20);

  //  read duration of echo
  int duration = pulseIn(pinEcho, HIGH);

  if(duration > 0) {
    // dist = duration * speed of sound * 1/2
    // dist in cm = duration in us * 1 x 10^{-6} * 340.26 * 100 * 1/2
    // =  0.017*duration
    float dist = 0.017 * duration;
    Serial.println(dist);

    if (dist < 10.00) {
      digitalWrite(led, HIGH);
    }
    else {
      digitalWrite(led, LOW);
    }
  }

  // wait
  delay(70);
}
