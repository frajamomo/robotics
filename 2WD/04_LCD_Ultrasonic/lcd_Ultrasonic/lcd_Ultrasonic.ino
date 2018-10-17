#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

#define TRIG_PIN 2    // Trigger
#define ECHO_PIN 3    // Echo

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


//Crear el objeto lcd  dirección  0x3F y 16 columnas x 2 filas
LiquidCrystal_I2C lcd(0x3F,16,2);  //

void setup() {

  Serial.begin (9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  
  // Inicializar el LCD
  lcd.init();
  
  //Encender la luz de fondo.
  lcd.backlight();
  
  // Escribimos el Mensaje en el LCD.
  lcd.print("Hola Mundo");
}

void loop() {

  distancia = getDistance(TRIG_PIN,ECHO_PIN);

  if (distancia < 10) {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else {
    digitalWrite(LED_BUILTIN, LOW);
  }

  Serial.println(distancia);// put your main code here, to run repeatedly:

  char msg[17];
  sprintf(msg, "Distancia: %3d", distancia);
  lcd.setCursor(0, 0);
  lcd.print(msg);
  

  
   // Ubicamos el cursor en la primera posición(columna:0) de la segunda línea(fila:1)
  lcd.setCursor(0, 1);
   // Escribimos el número de segundos trascurridos
  lcd.print(millis()/1000);
  lcd.print(" Segundos");
  delay(100);

  
}
