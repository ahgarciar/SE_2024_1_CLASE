void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}

String cad = "Ex";
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    cad = Serial.readString();    
  }
  Serial.println("echo: " + cad);
  delay(500);
}
