int led = 13; //pin 13 del arduino 

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT); //INPUT   OUTPUT
  Serial.begin(9600);  //vel por defecto usada por arduino ..
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, 1);  //1 prender  0 = apagar  HIGH / LOW
  Serial.println("LED ENCEDIDO");
  delay(1000);
  digitalWrite(led, 0);
  Serial.println("LED APAGADO");
  delay(1000);
}
