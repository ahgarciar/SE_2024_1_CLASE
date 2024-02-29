int led = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100); //ms
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v= Serial.readString().toInt();
    digitalWrite(led, v);
  }
  delay(100);

}
