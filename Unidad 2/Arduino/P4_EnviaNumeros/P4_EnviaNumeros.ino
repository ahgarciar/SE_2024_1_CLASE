void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int numero = analogRead(A0); 
  Serial.println(String(numero));
  delay(1000); //ms
}
