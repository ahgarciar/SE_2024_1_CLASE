int sensor = A0; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int lecturas = 10;
int contLecturas = 0;
int valor = 0;
int res = 0;
void loop() {
  // put your main code here, to run repeatedly:
  for(contLecturas = 0; contLecturas < lecturas; contLecturas++){      
      valor = analogRead(sensor);
      res += valor;
      delayMicroseconds(10);
  }
  res /= lecturas;
  delay(500); 
}
