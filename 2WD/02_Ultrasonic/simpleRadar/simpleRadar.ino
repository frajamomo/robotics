
/* Declaramos las variables */
long distancia;
long tiempo;

void setup() {
  Serial.begin(9600);
  /* Declaramos el pin 9 como salida del pulso ultrasonico */
  pinMode(9, OUTPUT);
  /* Declaramos el pin 8 como entrasa (tiempo que tarda en volver) */
  pinMode(8, INPUT);
  /* Declaramos el pin 12 como el pin del LED */
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

  /* Se estabiliza el sensor */
  digitalWrite(9, LOW);
  delayMicroseconds(5);
  /* Se envia el pulso ultrasonico */
  digitalWrite(9, HIGH);
  delayMicroseconds(10);
  /* Mide el tiempo transcurrido entre la salida y la llegada del pulso ultrasonico */
  tiempo = pulseIn(8, HIGH);
  /* Se calcula la distancia on esta formila*/
  distancia = int(0.017 * tiempo);
  /* Si la distancia es menor a 15 centimetros prendemos el led */
  if (distancia < 15)
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  /* Si la distancia es mayor a 15 centimetros, el led permanece apagado */
  else
  {
    digitalWrite(LED_BUILTIN, LOW);
  }
  /* Se imprime la distancia en centimetros en el monitor serial */
  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");

  delay(200);
}
