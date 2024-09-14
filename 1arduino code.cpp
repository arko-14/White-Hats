const int ledPins[6] = {12, 11, 10, 9, 8, 7};  // Define the LED pins

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 6; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    char binaryCode[7];
    Serial.readBytes(binaryCode, 6);
    binaryCode[6] = '\0';  // Null-terminate the string

    for (int i = 0; i < 6; i++) {
      if (binaryCode[i] == '1') {
        digitalWrite(ledPins[i], HIGH);
      } else {
        digitalWrite(ledPins[i], LOW);
   }
}
}
}
