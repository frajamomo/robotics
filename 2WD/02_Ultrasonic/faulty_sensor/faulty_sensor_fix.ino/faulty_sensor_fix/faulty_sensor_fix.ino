
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

void setup() {
    Serial.begin (9600);
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    pinMode(LED_BUILTIN, OUTPUT);
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
  delay(200);
}
