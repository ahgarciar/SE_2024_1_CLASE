int pot = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int valor = analogRead(pot);
  Serial.println(valor); // 0 - 1023 
  delay(500);
}
