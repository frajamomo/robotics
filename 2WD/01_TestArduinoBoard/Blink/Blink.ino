/*
  Blink
  http://www.arduino.cc/en/Tutorial/Blink
  Board: Arduino Nano
  Processor: ATmega328P(Old Bootloader)
  Programer: "Arduino as ISP"
*/
const int DUTY_CYCLE = 1000;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(DUTY_CYCLE / 2);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(DUTY_CYCLE / 2);                       // wait for a second
}
