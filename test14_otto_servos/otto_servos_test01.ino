// External power supply

#include <Servo.h>

Servo Pierna_Derecha;
Servo Pierna_Izquierda;
Servo Pie_Derecho;
Servo Pie_Izquierdo;

int minim = 0;
int maxim = 180;
int recto = 90;

void setup() {
  Pierna_Derecha.attach(2);
  Pierna_Izquierda.attach(3);
  Pie_Derecho.attach(4);
  Pie_Izquierdo.attach(5);

  Pierna_Derecha.write(minim);
  delay(3000);
  Pierna_Derecha.write(maxim);
  delay(3000);
  Pierna_Derecha.write(recto);
  delay(3000);

  Pierna_Izquierda.write(minim);
  delay(3000);
  Pierna_Izquierda.write(maxim);
  delay(3000);
  Pierna_Izquierda.write(recto);
  delay(3000);

  Pie_Derecho.write(minim);
  delay(3000);
  Pie_Derecho.write(maxim);
  delay(3000);
  Pie_Derecho.write(recto);
  delay(3000);

  Pie_Izquierdo.write(minim);
  delay(3000);
  Pie_Izquierdo.write(maxim);
  delay(3000);
  Pie_Izquierdo.write(recto);
  delay(3000);

  Pierna_Derecha.write(recto);
  Pierna_Izquierda.write(recto);
  Pie_Derecho.write(recto);
  Pie_Izquierdo.write(recto);
}

void loop() {
//  Pierna_Derecha.write(recto);
//  Pierna_Izquierda.write(recto);
//  Pie_Derecho.write(recto);
//  Pie_Izquierdo.write(recto);
}
