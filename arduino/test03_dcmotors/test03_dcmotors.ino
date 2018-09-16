// Demo program for the Dagu Arduino Mini Driver. Uses dead reckoning 
// to try to drive a robot in a square

const int LEFT_MOTOR_DIR_PIN = 7;
const int LEFT_MOTOR_PWM_PIN = 9;
const int RIGHT_MOTOR_DIR_PIN = 8;
const int RIGHT_MOTOR_PWM_PIN = 10;

const int DRIVE_FORWARD_TIME_MS = 1500;
const int TURN_TIME_MS = 2000;

// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
const int led = 13;

//----------------------------------------------------------
void setup()
{
    // Setup the pins
    pinMode( LEFT_MOTOR_DIR_PIN, OUTPUT );
    pinMode( LEFT_MOTOR_PWM_PIN, OUTPUT );
    pinMode( RIGHT_MOTOR_DIR_PIN, OUTPUT );
    pinMode( RIGHT_MOTOR_PWM_PIN, OUTPUT );
    pinMode( led, OUTPUT);
}

//----------------------------------------------------------
void loop()
{
    // Drive forwards at 100%
    digitalWrite(led, HIGH);
    digitalWrite( LEFT_MOTOR_DIR_PIN, HIGH );
    digitalWrite( RIGHT_MOTOR_DIR_PIN, HIGH );
    analogWrite( LEFT_MOTOR_PWM_PIN, 100 );
    analogWrite( RIGHT_MOTOR_PWM_PIN, 100 );
    delay( DRIVE_FORWARD_TIME_MS );

    // Turn left at 50%
    digitalWrite(led, LOW);
    digitalWrite( LEFT_MOTOR_DIR_PIN, HIGH );
    digitalWrite( RIGHT_MOTOR_DIR_PIN, LOW );
    analogWrite( LEFT_MOTOR_PWM_PIN, 50 );
    analogWrite( RIGHT_MOTOR_PWM_PIN, 50 );
    delay( TURN_TIME_MS );
}
