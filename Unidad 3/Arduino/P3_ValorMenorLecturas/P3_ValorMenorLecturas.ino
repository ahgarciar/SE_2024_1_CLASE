int sensor = A0; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int lecturas = 10;
int contLecturas = 0;
int valor = 0;
int valorMenor = 1024;
void loop() {
  // put your main code here, to run repeatedly:  
  for(contLecturas = 0; contLecturas < lecturas; contLecturas++){      
      valor = analogRead(sensor);
      if(valor < valorMenor){ valorMenor = valor;      }
      delayMicroseconds(10);
  }
  Serial.println(valorMenor);
  delay(500); 
}
