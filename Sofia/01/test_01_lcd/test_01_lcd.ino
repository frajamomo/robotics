#include <Wire.h>
#include <LiquidCrystal_I2C.h>

//Crear el objeto lcd  dirección  0x3F y 16 columnas x 2 filas
LiquidCrystal_I2C lcd(0x3F,16,2);  //

void setup() {

  Serial.begin (9600);
  pinMode(LED_BUILTIN, OUTPUT);

  // Inicializar el LCD
  lcd.init();

  //Encender la luz de fondo.
  lcd.backlight();

  // Escribimos el Mensaje en el LCD.
  lcd.print("Hola Sofia");
  delay(1000);
}

void loop() {
  // Escribimos el número de segundos trascurridos
  lcd.setCursor(0,1);
  lcd.print(millis()/1000);
  lcd.print(" Segundos");
  delay(100);
}
