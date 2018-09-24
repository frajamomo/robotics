// Same funcionality as test05 but with functions
//
#include "Arduino.h"

int pinTrigger = 2;
int pinEcho = 4;
int led = 13;

const int LEFT_MOTOR_DIR_PIN = 7;
const int LEFT_MOTOR_PWM_PIN = 9;
const int RIGHT_MOTOR_DIR_PIN = 8;
const int RIGHT_MOTOR_PWM_PIN = 10;

const int DRIVE_FORWARD_TIME_MS = 1500;
const int TURN_TIME_MS = 2000;

const float OUT_OF_RANGE_DISTANCE = 50.00;

float getDistance()
{
  float dist = OUT_OF_RANGE_DISTANCE;
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
    dist = 0.017 * duration;
  }
  return dist;
}


void setup()
{
  // initialize serial comms
  Serial.begin(9600);

  // set pins
  pinMode(pinTrigger, OUTPUT);
  pinMode(pinEcho, INPUT);
  pinMode(led, OUTPUT);

  // Setup the pins
  pinMode( LEFT_MOTOR_DIR_PIN, OUTPUT );
  pinMode( LEFT_MOTOR_PWM_PIN, OUTPUT );
  pinMode( RIGHT_MOTOR_DIR_PIN, OUTPUT );
  pinMode( RIGHT_MOTOR_PWM_PIN, OUTPUT );
}

void loop()
{
    float dist = getDistance();
    Serial.println(dist);

    if (dist < 10.00) {
      digitalWrite(led, HIGH);
      // Drive forwards at 100%
      digitalWrite( LEFT_MOTOR_DIR_PIN, HIGH );
      digitalWrite( RIGHT_MOTOR_DIR_PIN, HIGH );
      analogWrite( LEFT_MOTOR_PWM_PIN, 100 );
      analogWrite( RIGHT_MOTOR_PWM_PIN, 100 );
    }
    else if ((dist > 10.00) and (dist < 20.00)) {
      // Drive forwards at 50%
      digitalWrite( LEFT_MOTOR_DIR_PIN, HIGH );
      digitalWrite( RIGHT_MOTOR_DIR_PIN, HIGH );
      analogWrite( LEFT_MOTOR_PWM_PIN, 50 );
      analogWrite( RIGHT_MOTOR_PWM_PIN, 50 );
    }
    else {
      digitalWrite(led, LOW);
      // Stop motors
      digitalWrite( LEFT_MOTOR_DIR_PIN, HIGH );
      digitalWrite( RIGHT_MOTOR_DIR_PIN, HIGH );
      analogWrite( LEFT_MOTOR_PWM_PIN, 0 );
      analogWrite( RIGHT_MOTOR_PWM_PIN, 0 );

    }
  }

  // wait
  delay(70);
}
