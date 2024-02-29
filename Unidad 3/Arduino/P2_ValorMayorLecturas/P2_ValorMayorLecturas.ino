int sensor = A0; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int lecturas = 10;
int contLecturas = 0;
int valor = 0;
int valorMayor = -1;
void loop() {
  // put your main code here, to run repeatedly:  
  for(contLecturas = 0; contLecturas < lecturas; contLecturas++){      
      valor = analogRead(sensor);
      if(valor > valorMayor){ valorMayor = valor;      }
      delayMicroseconds(10);
  }
  Serial.println(valorMayor);
  delay(500); 
}
