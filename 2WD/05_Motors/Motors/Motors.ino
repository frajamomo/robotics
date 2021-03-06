#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <L298N.h>

//pin definition for the HC-SR04 ultrasonic distance sensor
#define TRIG_PIN 2    // Trigger
#define ECHO_PIN 3    // Echo

//pin definition for the L298n motor driver
#define EN_Right 10
#define IN1_Right 9
#define IN2_Right 8
#define EN_Left 5
#define IN3_Left 7
#define IN4_Left 6

//create a motor instance
L298N motorRight(EN_Right, IN1_Right, IN2_Right);
L298N motorLeft(EN_Left, IN3_Left, IN4_Left);

//Create the LCD with 0x3F address and 16x2 size
LiquidCrystal_I2C lcd(0x3F, 16, 2); //

const unsigned long DUTY_INTERVAL = 200;
unsigned long gLastCommandTime = 0;
long distancia;

int getDistance(int trigPin, int echoPin) // returns the distance (cm)
{
  long duration, distance;

  digitalWrite(trigPin, HIGH); // We send a 10us pulse
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH, 20000); // We wait for the echo to come back, with a timeout of 20ms, which corresponds approximately to 3m

  // pulseIn will only return 0 if it timed out. (or if echoPin was already to 1, but it should not happen)
  if (duration == 0) // If we timed out
  {
    pinMode(echoPin, OUTPUT); // Then we set echo pin to output mode
    digitalWrite(echoPin, LOW); // We send a LOW pulse to the echo pin
    delayMicroseconds(200);
    pinMode(echoPin, INPUT); // And finaly we come back to input mode
  }

  distance = (duration / 2) / 29.1; // We calculate the distance (sound speed in air is aprox. 291m/s), /2 because of the pulse going and coming

  return distance; //We return the result. Here you can find a 0 if we timed out
}
void retroceder() {
  motorRight.setSpeed(200);
  motorLeft.setSpeed(200);
  motorRight.backward();
  motorLeft.backward();
  delay(1500);
  motorRight.stop();
  motorLeft.stop();
}

void girar() {
  motorRight.setSpeed(150);
  motorRight.backward();
  delay(500);
  motorRight.stop();
}

void setup() {

  Serial.begin (9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  // Inicializar el LCD
  lcd.init();

  //Encender la luz de fondo.
  lcd.backlight();

  motorRight.setSpeed(150); // an integer between 0 and 255
  motorLeft.setSpeed(150); // an integer between 0 and 255
}

void loop() {
  unsigned long curTime = millis();
  if ( curTime - gLastCommandTime > DUTY_INTERVAL )
  {

    distancia = getDistance(TRIG_PIN, ECHO_PIN);

    if (distancia < 10) {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else {
      digitalWrite(LED_BUILTIN, LOW);
    }

    char line0[17];
    sprintf(line0, "Distancia: %3d", distancia);
    lcd.setCursor(0, 0);
    lcd.print(line0);

    // Ubicamos el cursor en la primera posición(columna:0) de la segunda línea(fila:1)
    lcd.setCursor(0, 1);
    // Escribimos el número de segundos trascurridos
    lcd.print(millis() / 1000);
    lcd.print(" Segundos");

    if ((distancia == 0) or (distancia > 20)) {
      // FULL SPEED
      motorRight.setSpeed(150); // an integer between 0 and 255
      motorLeft.setSpeed(150); // an integer between 0 and 255
      motorRight.forward();
      motorLeft.forward();
    }
    else if ((distancia > 15.00) and (distancia < 20.00)) {
      motorRight.setSpeed(100); // an integer between 0 and 255
      motorLeft.setSpeed(100); // an integer between 0 and 255
      motorRight.forward();
      motorLeft.forward();
    }
    else if (distancia < 15.00) {
      motorRight.stop();
      motorLeft.stop();
      retroceder();
      girar();
    }

    gLastCommandTime = millis();
  }

}
