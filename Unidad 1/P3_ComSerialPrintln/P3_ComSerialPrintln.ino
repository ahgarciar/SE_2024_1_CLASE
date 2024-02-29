
void setup() {
  // put your setup code here, to run once:
  //modulo de comunicacion serial --- > UART ...
  // inicializacion:
  Serial.begin(9600); //baudios

 }

void loop() { //16mhz
  // put your main code here, to run repeatedly:

  Serial.println("Hola");
  delay(500); //ms

}
