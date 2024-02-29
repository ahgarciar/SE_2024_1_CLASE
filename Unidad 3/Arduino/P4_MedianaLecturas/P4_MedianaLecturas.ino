int sensor = A0; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int lecturas = 10;
int contLecturas = 0;
int valor[10]; // = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
void loop() {
  // put your main code here, to run repeatedly:  
  for(contLecturas = 0; contLecturas < lecturas; contLecturas++){      
      valor[contLecturas] = analogRead(sensor);      
      delayMicroseconds(10);
  }
  ///
  for(int i=0; i<lecturas-1; i++){
    for(int j = i+1; j<lecturas;j++){
      if (valor[i] < valor[j]){
        int aux = valor[i];
        valor[i] = valor[j];
        valor[j] = aux;
      }
    }
  }
  ///
  Serial.println(valor[lecturas/2]);
  delay(500); 
}
